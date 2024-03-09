import scrapy
import json
from ..items import PeriodictableItem


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
        columns = data.get("Table").get("Columns").get("Column")
        rows = data.get("Table").get("Row")

        for i in rows:
            cells = i.get("Cell")

            for (column, row) in zip(columns, cells):
                periodic_table = PeriodictableItem()

                column = periodic_table["column"]
                row = periodic_table["row"]

                yield periodic_table
