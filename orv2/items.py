# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join, Identity, Compose

from orv2.spiders.utils import date_handler, html_handler

class RestItem(scrapy.Item):
    ID = scrapy.Field()     # ID
    TT = scrapy.Field()     # Title
    NM = scrapy.Field()     # Name
    RT = scrapy.Field()     # Rating
    BM = scrapy.Field()     # Bookmarked
    DT = scrapy.Field()     # District
    PR = scrapy.Field()     # PriceRange
    TP = scrapy.Field()     # Type
    RC = scrapy.Field()     # ReviewCount
    OS = scrapy.Field()     # Overall Smile Count
    OO = scrapy.Field()     # Overall OK Count
    OC = scrapy.Field()     # Overall Cry Count
    AT = scrapy.Field()     # Aspect Taste Rating
    AD = scrapy.Field()     # Aspect Decor Rating
    AH = scrapy.Field()     # Aspect Hygiene Rating
    AS = scrapy.Field()     # Aspect Service Rating
    AV = scrapy.Field()     # Aspect Value Rating

class RestLoader(ItemLoader):
    default_input_processor = MapCompose(int)
    default_output_processor = TakeFirst()

    TT_in = MapCompose(str)
    NM_in = MapCompose(str)
    DT_in = MapCompose(str) # Date Filter
    TP_in = MapCompose(str)

    RT_in = MapCompose(float)

    TP_out = Join("|")



class RevItem(scrapy.Item):
    ID = scrapy.Field()     # ID
    RI = scrapy.Field()     # Restaurant ID
    UI = scrapy.Field()     # User ID
    DA = scrapy.Field()     # Date
    OR = scrapy.Field()     # Overall
    VC = scrapy.Field()     # View Count
    TT = scrapy.Field()     # Title
    BD = scrapy.Field()     # Body
    TE = scrapy.Field()     # Title Emoji
    CE = scrapy.Field()     # Custom Emoji
    BE = scrapy.Field()     # Body Emoji
    UR = scrapy.Field()     # Picture URL

    DV = scrapy.Field()     # Date of Visit
    WT = scrapy.Field()     # Waiting Time
    DM = scrapy.Field()     # Dining Method
    SP = scrapy.Field()     # Spending Per Head
    TM = scrapy.Field()     # Type of Meal
    CB = scrapy.Field()     # Celebration
    DO = scrapy.Field()     # Dining Offer

    AT = scrapy.Field()     # Aspect Taste Rating
    AD = scrapy.Field()     # Aspect Decor Rating
    AH = scrapy.Field()     # Aspect Hygiene Rating
    AS = scrapy.Field()     # Aspect Service Rating
    AV = scrapy.Field()     # Aspect Value Rating

class RevLoader(ItemLoader):
    default_input_processor = MapCompose(int)
    default_output_processor = TakeFirst()

    SP_in = MapCompose(float)

    TT_in = MapCompose(str)
    BD_in = MapCompose(str)
    UR_in = MapCompose(str)
    OR_in = MapCompose(str)
    DO_in = MapCompose(str)
    DA_in = MapCompose(date_handler)
    BD_in = MapCompose(html_handler)

    TE_in = MapCompose(str) # Date Filter
    CE_in = MapCompose(str)
    BE_in = MapCompose(str)

    DV_in = MapCompose(str)
    DM_in = MapCompose(str)
    TM_in = MapCompose(str)
    CB_in = MapCompose(str)

    UR_out = Join("|")
    CE_out = Join("|")
    DO_out = Join("|")
