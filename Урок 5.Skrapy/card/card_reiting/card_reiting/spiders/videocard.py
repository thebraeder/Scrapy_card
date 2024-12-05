import scrapy

class VideocardSpider(scrapy.Spider):
    name = "videocard"
    allowed_domains = ["technical.city"]
    start_urls = ["https://technical.city/ru/video/rating"]

    def parse(self, response):
        rows = response.xpath("//tr")
        for row in rows:
            name = row.xpath(".//td[2]/a/text()").get()  # Название видеокарты
            performance = row.xpath(".//td[4]/text()").get()  # Производительность
            year = row.xpath(".//td[6]/text()").get()  # Год выпуска
            wattage = row.xpath(".//td[7]/text()").get()  # Ватты

            if name:  # Чтобы пропускать пустые строки
                yield {
                    'card_name': name.strip(),
                    'performance': performance.strip() if performance else None,
                    'year': year.strip() if year else None,
                    'wattage': wattage.strip() if wattage else None,
                }