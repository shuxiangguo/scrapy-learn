import scrapy
from ..items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = "zufang"
    start_urls = [
        'http://bj.ganji.com/fang1/chaoyang/'
    ]

    def parse(self, response):
        # print(response)
        zf = ZufangItem()
        title_list = response.css("dd.title a::text").extract()
        money_list = response.css("div.price span.num::text").extract()
        for i, j in zip(title_list, money_list):
            zf['title'] = i
            zf['money'] = j
            yield zf
        #     print(i, ":", j)

        # yield {
        #     "title_list": response.css("dd.title a::text").extract(),
        #     "money_list":  response.css("div.price span.num::text").extract(),
        # }
