# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from sunDetributeSpider.items import SundetributespiderItem


class Sun2Spider(RedisSpider):
    name = 'sun2'
    # allowed_domains = ['wz.sun0769.com']
    # start_urls = ['http://wz.sun0769.com/']
    # 起始地址：lpush sun2:start_urls http://wz.sun0769.com/index.php/question/questionType?type=4&page=
    redis_key = 'sun2:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Sun2Spider, self).__init__(*args, **kwargs)
        self.url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
        self.offset = 0

    def parse(self, response):
        self.log('——————————————————————————————————开始解析网页————————————————————————————————')
        # print(response.body)
        # 每一行信息
        msg_list = response.xpath('//div[@class="greyframe"]/table[2]//table/tr')
        print(len(msg_list))

        for each in msg_list:
            item = SundetributespiderItem()
            # 编号
            item['id'] = each.xpath('./td[1]/text()').extract()[0].strip()

            # 标题
            item['title'] = each.xpath('./td[2]/a[2]/text()').extract()[0].strip()

            # 标题链接
            item['title_url'] = each.xpath('./td[2]/a[2]/@href').extract()[0].strip()

            # 投诉者
            item['complainant'] = each.xpath('./td[4]/text()').extract()[0].strip()

            # 投诉时间
            item['complain_time'] = each.xpath('./td[5]/text()').extract()[0].strip()

            # 投诉详情
            req = scrapy.Request(item['title_url'], callback=self.parse_item, dont_filter=True)
            req.meta['item'] = item
            yield req

        # 翻页，设置翻页条件
        if self.offset <= 8000:
            self.offset += 30
            print('next page url:', self.url + str(self.offset))
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)

    def parse_item(self, response):
        print('parse item:', response.url)
        item = response.meta['item']
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()
        yield item
