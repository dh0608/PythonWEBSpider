from scrapy import cmdline  # 命令行

# 执行的文件名
name = 'douyu1'
# 执行的命令
cmd = f'scrapy crawl {name}'
# 命令行执行命令
cmdline.execute(cmd.split())