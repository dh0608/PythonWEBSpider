# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from sunDetributeSpider.items import SundetributespiderItem


class Sun1Spider(CrawlSpider):
    name = 'sun1'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    # 翻页的链接
    page_url = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]',))
    # 详情页链接
    title_url = LinkExtractor(restrict_xpaths=('//a[@class="news14"]',))
    # 提取规则
    rules = [
        Rule(page_url, follow=True),
        Rule(title_url, callback='parse_item')
    ]

    def parse_item(self, response):
        item = SundetributespiderItem()
        # 标题
        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0]
        # URL
        item['title_url'] = response.url
        # 编号
        item['id'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].split(':')[
            -1]
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()
        # 作者
        temp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        temp = temp.split(' ')
        item['complainant'] = temp[0].split('：')[-1]
        # 投诉时间
        item['complain_time'] = temp[1].split('：')[-1] + ' ' + temp[2]
        yield item
