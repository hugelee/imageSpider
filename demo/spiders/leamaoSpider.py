from scrapy.spider import BaseSpider
import scrapy
from demo.items import ImageItem
from scrapy.utils.url import urljoin_rfc
class MyImageSpider(BaseSpider):
    start_urls = []
    name = "lesmao_spider"
    start_urls = [
        "http://www.lesmao.com",
    ]

    def parse(self, response):
        url_set = set()
        item = ImageItem()
        next_urls =[]
        item['image_urls'] = response.xpath('//div/ul/li/img/@src').extract()
        yield item
        next_page_urls = response.xpath('//div[@class="photo"]/a/@href').extract()
        next_inner_urls = response.xpath('//div[@id="thread-page"]/a/@href').extract()
        next_front_url = response.xpath('//div[@class="pg"]/a[@class="vpn"]/@href').extract()[-1]
#        next_urls = next_page_urls + next_inner_urls
#        next_urls.append(next_inner_urls)
#        next_urls.append(next_page_urls)
        next_urls = next_inner_urls + next_page_urls
        next_urls.append(next_front_url)
        print next_urls
        for one_url in next_urls:
            if one_url not in url_set and one_url is not None:
                url_set.add(one_url) 
                print "================================="
                print one_url
                print "================================="
                yield scrapy.Request(response.urljoin(one_url))
            else:
                print "================================="
                print "this url is old",one_url
                print "================================="