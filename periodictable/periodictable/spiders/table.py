import scrapy


class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["pubchem.ncbi.nlm.nih.gov/ptable"]

    def start_requests(self):

        yield scrapy.Request(
            url="https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON",
            method="GET",
            # body=json.dumps(query),
            headers={
                "Content-Type": "application/json"
            },
            callback=self.parse
        )

    def parse(self, response):
        print(response.body)

