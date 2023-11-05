import scrapy
import json

class PlaystationSpider(scrapy.Spider):
    name = "ps_spider"
    allowed_domains = ["store.playstation.com"]
    start_urls = ["https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/2"] 

    def parse(self, response):
        games = response.css('a[data-telemetry-meta]')  

        for game in games:
            meta_data = json.loads(game.attrib['data-telemetry-meta'])
            title = meta_data['name']
            price = meta_data['price']

            yield {
                'title': title,
                'price': price
            }