from scrapy.spider import BaseSpider
import scrapy
from demo.items import ImageItem
from scrapy.utils.url import urljoin_rfc
class MyImageSpider(scrapy.Spider):
    start_urls = []
    name = "image_spider"
    tags = range(49,79)
    for i in tags:
        tag_url = "http://www.ugirls.com/Index/Search/Magazine-" + str(i) + ".html"
        start_urls.append(tag_url)
#    start_urls = [
#        "http://www.ugirls.com/Index/Search/Magazine-49.html",
#    ]

    def parse(self, response):
        item = ImageItem()
        url_set = set()
        item['image_urls'] = response.xpath('//img[contains(@src, "magazine_web_m.jpg")]/@src').extract()
        yield item
        next_urls = response.xpath('//ul/li/a[contains(@href, "-")]/@href').extract()
        for one_url in next_urls:
            if one_url not in url_set:
                url_set.add(one_url)
                yield scrapy.Request(response.urljoin(one_url)) 
        with open('./urls','a') as f:
            for i in url_set:
                f.write(str(i))
#            print one_url
#        yield item