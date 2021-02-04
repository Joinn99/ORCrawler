import scrapy
import sqlite3
import pandas as pd
from tqdm import tqdm
from scrapy.loader import ItemLoader
from orv2.items import RestItem, RevItem, RestLoader, RevLoader
from orv2.spiders.reg import EMOJI_REG
from orv2.spiders.utils import info_handler

class orv2(scrapy.Spider):
    name = 'orv2'
    allowed_domains = ['openrice.com']

    def __init__(self):
        '''
        Initilization
        '''
        self.url = 'https://www.openrice.com/en/hongkong/r-openrice-r{:s}/reviews'

    def start_requests(self):
        '''
        Run the crawling.
        '''
        ## Iteration
        conn = sqlite3.connect("Meta/ORID.sqlite")
        while True:
            restID = pd.read_sql("SELECT ID FROM rid WHERE state=1 LIMIT 1", conn)["ID"]
            if restID.empty:
                print("Finished.")
                conn.close()
            else:
                print("ID: {:d} |".format(restID[0]), end=".")
                yield scrapy.Request(self.url.format(str(restID[0])))
                conn.execute("UPDATE rid SET State=0 WHERE ID={:d}".format(restID[0]))
                conn.commit()
                print("Success.")
                


    def parse(self, response):
        review_list = response.xpath("//div[@itemprop='review']")
        for review in review_list:
            yield self._parse_rev(review)

        if response.xpath("//div[@class='or-sprite common_pagination_more_r_desktop']"):
            print(".", end="")
            next_url = response.xpath("//div[@class='or-sprite common_pagination_more_r_desktop']/../@href").get()
            yield scrapy.Request('https://www.openrice.com/' + next_url)
        else:
            yield self._parse_rest(response)

    def _parse_rest(self, response):
        loader = RestLoader(item = RestItem(), response=response)

        loader.add_xpath('ID', "//div[@itemprop='itemReviewed']/div/div/@data-poi-id")
        loader.add_xpath('TT', "//ul[@class='breadcrumb']/li[5]/a/span/text()")
        loader.add_xpath('NM', "//div[@class='poi-name']/h1/span/text()")
        loader.add_xpath('RT', "//div[@class='header-score']/text()")
        loader.add_xpath('BM', "//div[@class='header-bookmark-count js-header-bookmark-count']/@data-count")
        loader.add_xpath('DT', "//ul[@class='breadcrumb']/li[4]/a/span/text()")
        loader.add_xpath('PR', "//div[@itemprop='priceRange']/a/@href", re=r"(?<==).")
        loader.add_xpath('TP', "//div[@class='header-poi-categories dot-separator']/a/@href", re=r"(?<=/)[^/]+$")
        loader.add_xpath('RC', "//span[@itemprop='reviewCount']/text()")
        loader.add_xpath('OS', "//div[@class='score-div'][1]/text()")
        loader.add_xpath('OO', "//div[@class='score-div'][2]/text()")
        loader.add_xpath('OC', "//div[@class='score-div'][3]/text()")

        for aspect in response.xpath("//div[@class='header-score-details-right-item']"):
            loader.add_value('A' + aspect.xpath("div[@class='header-score-details-right-item-title']/text()").re(r"^[TDHSV]")[0],
                                aspect.xpath("div[2]/@class").re(r"[1-5](?=0_red_s$)"))
        return loader.load_item()

    def _parse_rev(self, response):
        loader = RevLoader(item = RevItem(), selector=response)
        
        loader.add_xpath('ID', "@data-review-id")
        loader.add_xpath('RI', "@data-poi-id")
        loader.add_xpath('UI', "div//a[@itemprop='author']", re=(r"(?<=id=)[0-9]+"))
        loader.add_xpath('DA', "div//span[@itemprop='datepublished']/text()")
        loader.add_xpath('OR', "div//div[@class='left-header']/div/@class", re=r"(?<=smiley_)[a-z]+(?=_)")
        loader.add_xpath('VC', "div//span[@class='view-count']/text()", re=r"[0-9]+")
        loader.add_xpath('TT', "div//div[@class='review-title']/a/text()")
        loader.add_xpath('BD', "div//section[@class='review-container']")
        loader.add_xpath('TE', "div//div[@class='review-title']/a/text()", re=EMOJI_REG)
        loader.add_xpath('CE', "div//section[@class='review-container']/div[@class[contains(., 'write-re-icon')]]/@class", re=r"(?<=icon-).+$")
        loader.add_xpath('BE', "div//section[@class='review-container']/text()", re=EMOJI_REG)
        loader.add_xpath('UR', "div//a[@data-is-photo='true']/@data-shorten-url", re=r"(?<=/)[0-9|A-Z|a-z]+$")

        for aspect in response.xpath("div//section[@class='sr2-review-list2-detailed-rating-section detail']/div[@class='subject']"):
            loader.add_value('A' + aspect.xpath("div[1]/text()").re(r"^[TDHSV]")[0], aspect.xpath("div[2]/span/@class").re(r"(?<=on_)[gy]").count('y'))
        
        for (attr, value) in info_handler(response.xpath("div//section[@class='info-section detail']/section[@class='info info-row']")):
            loader.add_value(attr, value)
        
        return loader.load_item()
