from scrapy import cmdline
name = 'dmoz'
# name = 'mycrawler_redis'
# name = 'myspider_redis'
cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())





