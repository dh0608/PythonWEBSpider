from pyppeteer import launch
import requests
import asyncio

# url = 'http://quotes.toscrape.com/js/'
# response = requests.get(url, verify=False)
# html = response.text
# print(html)
# 可以发现这种方式不能读取网页信息，发现是js动态加载的

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())


