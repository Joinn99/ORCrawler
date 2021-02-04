# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import gzip
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem


class GzipCsvItemExporter(CsvItemExporter):
    def __init__(self, stream, **kwargs):
        self.gzfile = gzip.GzipFile(fileobj=stream)
        super(GzipCsvItemExporter, self).__init__(self.gzfile, **kwargs)

    def finish_exporting(self):
        self.gzfile.close()

class Orv2Pipeline:
    def open_spider(self, spider):
        self.rest_exporter = GzipCsvItemExporter(open('Data/rest.csv.gz', 'wb'))
        self.review_exporter = GzipCsvItemExporter(open('Data/review.csv.gz', 'wb'))
        self.rest_exporter.start_exporting()
        self.review_exporter.start_exporting()

    def close_spider(self, spider):
        self.rest_exporter.finish_exporting()
        self.review_exporter.finish_exporting()

    def process_item(self, item, spider):
        if item.__class__.__name__ == "RevItem":
            self.review_exporter.export_item(item)
        else:
            self.rest_exporter.export_item(item)
        return item
