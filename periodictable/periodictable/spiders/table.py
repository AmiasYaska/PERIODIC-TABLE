import scrapy


class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["pubchem.ncbi.nlm.nih.gov"]
    start_urls = ["https://pubchem.ncbi.nlm.nih.gov"]

    def parse(self, response):
        pass
