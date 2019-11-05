from scrapy import cmdline
name = 'sun3'
cmd = f'scrapy crawl {name}'
cmdline.execute(cmd.split())