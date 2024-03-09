import scrapy
import json


class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["pubchem.ncbi.nlm.nih.gov/ptable"]

    def start_requests(self):

        yield scrapy.Request(
            url="https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON",
            method="GET",
            headers={
                "Content-Type": "application/json"
            },
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.body)
        column = data.get("Table").get("Columns").get("Column")
        row = data.get("Table").get("Row")

