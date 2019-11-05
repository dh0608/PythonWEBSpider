from scrapy import cmdline

# 执行的文件名
name = 'bmwx5'
# 执行的命令
cmd = f'scrapy crawl {name}'
# 命令行执行命令
cmdline.execute(cmd.split())