# -*- coding: utf-8 -*-
import scrapy
from JobSpider.items import JobspiderItem
import re


class PythonpositionSpider(scrapy.Spider):
    """
        爬取 51job 上海市的python岗位 信息
    """
    name = 'pythonPosition'
    allowed_domains = ['51job.com']
    start_urls = [
        'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def __init__(self, **kwargs):
        self.city = 10000
        self.max_city = 40000
        self.page = 1
        self.max_pages = 50
        self.str1 = r'https://search.51job.com/list/0'
        self.str2 = r',000000,0000,00,9,99,python,2,'
        self.str3 = r'.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    # 'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    start_urls = [
        'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def get_url(self):
        return self.str1 + str(self.city) + self.str2 + str(self.page) + self.str3

    def parse(self, response):
        self.log('——————————————————————————————————开始解析网页————————————————————————————————')
        # 页面代码
        # print(response.body)
        # 职位列表
        job_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        print(f'共有{len(job_list)}个职位')
        for item in job_list:
            # 每个 item 是一个对象，需要序列化转化字符串
            # 每个 item.xpath 返回的是一个列表，
            # 需要用 extract 进行序列化得到 Unicode 字符串

            # 职位名
            name = item.xpath('./p/span/a/text()').extract()[0].strip()
            print(f'职位名:{name}')

            # 公司名
            corp = item.xpath('./span[@class="t2"]/a/text()').extract()[0].strip()
            print(f'公司名:{corp}')

            # 工作地点
            city = item.xpath('./span[@class="t3"]/text()').extract()[0].strip()
            print(f'工作地点:{city}')

            # 薪资(不是全部都写有薪资)
            salary = item.xpath('./span[@class="t4"]/text()').extract()
            if len(salary) > 0:
                salary = salary[0].strip()
            else:
                salary = '面议'
            print(f'薪资:{salary}')

            # 发布时间
            pub_date = item.xpath('./span[@class="t5"]/text()').extract()[0].strip()
            print(f'发布时间:{pub_date}')

            print('=' * 120)

            # 将信息封装传入 items模块 中
            item = JobspiderItem()
            item['name'] = name
            item['corp'] = corp
            item['city'] = city
            item['salary'] = salary
            item['pub_date'] = pub_date

            p = self.str1 + r'(\d+).*'
            curcity = re.search(p, response.url).group(1)
            p = self.str1 + curcity + self.str2 + r'(\d+).*'
            # curpage = re.search(r'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,(\d+).*', response.url).group(1)
            curpage = re.search(p, response.url).group(1)
            self.page = int(curpage) + 1
            print('curpage ', self.page)
            print('curcity ', curcity)
            if self.page <= self.max_pages:
                url = self.get_url()
                # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
                yield scrapy.Request(url, callback=self.parse)
            else:
                self.city = int(curcity) + 10000
                if self.city <= self.max_city:
                    self.page = 1
                    url = self.get_url()
                    print('city ', self.city)
                    yield scrapy.Request(url, callback=self.parse)

                # 将获取的数据交给pipeline
                yield item

