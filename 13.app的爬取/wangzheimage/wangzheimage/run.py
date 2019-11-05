import scrapy.cmdline
name = 'hero1'
scrapy.cmdline.execute(f'scrapy crawl {name}'.split())

