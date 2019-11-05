import requests
from lxml import etree
from fake_useragent import UserAgent


class Amazon:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'x-wl-uid=1y1mr4/a+7GcF6tFTYtcvKEhqzTMIdAv0iK2YzgAdOP42+luT5C1p/kLkVu3RaVbntiTuO/0pDio=; session-id=459-0767606-0758848; ubid-acbcn=460-1155998-1778530; lc-acbcn=zh_CN; i18n-prefs=CNY; session-token=VsUz+OvrSoJltnpD7WhDGwEmjvZYmY8jihvVqGbj0KNdr0Zlw9ilauL+ijVlCR3SgHCAUUiOED4IMgjQLQLfbqnmqGK6XRwO2Kd6M1z7oDN+h4v6bf1IZpQNXGmZBfVgP1eW0dhcqZXBsGaMi3veqs8ulFCaxFPXyRUwbt/Sq5dteIKVUjncupV1TUgaaIgD; session-id-time=2082729601l; csm-hit=tb:A4A178FYPNJP0QP8M572+s-934KAW05B85QS1TZ6MTF|1563981287073&t:1563981287073&adb:adblk_no',
            'Host': 'www.amazon.cn',
            'Referer': 'https://www.amazon.cn/s?bbn=1755110071&rh=n%3A2016156051%2Cn%3A%212146610051%2Cn%3A%212146612051%2Cn%3A1755110071%2Cn%3A2152154051&dc&fst=as%3Aoff&qid=1563981234&rnid=2016157051&ref=lp_1755110071_nr_n_0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': UserAgent().random
        }

    def get_html(self, url):
        print(page_num)
        response = requests.get(url=url, headers=self.headers, verify=False)
        if int(response.status_code) > 400:
            print("当前:{}响应非200".format(url))
        else:
            self.deal_html(response.text)

    def deal_html(self, text):
        global page_num
        html = etree.HTML(text)
        divs = html.xpath('//div[@class="s-result-list s-search-results sg-row"]/div')
        for div in divs:
            img_url = ",".join(div.xpath('.//img/@src'))
            goos_url = "https://www.amazon.cn" + "".join(div.xpath('.//a[@class="a-link-normal a-text-normal"]/@href'))
            goos_title = "".join(div.xpath('.//a[@class="a-link-normal a-text-normal"]//span/text()'))
            goos_price = "-".join(
                div.xpath('.//span[@class="a-price-range aok-align-top"]//span[@class="a-offscreen"]/text()')).replace(
                "￥", "")
            print(goos_title, goos_price, goos_url, img_url)
        next_page_url = "https://www.amazon.cn" + "".join(html.xpath('//li[@class="a-last"]/a/@href'))
        page_num += 1
        self.get_html(next_page_url)


if __name__ == '__main__':
    page_num = 1
    amazon = Amazon()
    amazon.get_html(
        'https://www.amazon.cn/s?i=apparel&bbn=1755110071&rh=n%3A2016156051%2Cn%3A%212146610051%2Cn%3A%212146612051%2Cn%3A1755110071%2Cn%3A2152154051%2Cn%3A1768422071&dc&fst=as%3Aoff&qid=1563981244&rnid=2152154051&ref=sr_nr_n_24')
