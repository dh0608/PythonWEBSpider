import requests
from lxml import html
import csv
import codecs
etree = html.etree
"""
    1.网页的爬取
"""
url = 'http://tieba.baidu.com/f'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
name = input('请输入贴吧名称：')
start_page = int(input('请输入起始的页码：'))
end_page = int(input('请输入结束的页码：'))
for page in range(start_page, end_page+1):
    pn = (page - 1) * 50
    params = {
        'kw': name,
        'ie': 'utf-8',
        'pn': pn
    }
    r = requests.get(url, params=params, headers=headers)
    # 获取 html 页面内容
    html = r.text

    """
       2.数据的提取
    
    """

    # 将 html 字符串解析为 html 文档
    html = etree.HTML(html)
    # 获取帖子数对应的li标签
    TotalPosts = html.xpath('//li[contains(@class," j_thread_list clearfix")]')
    print('帖子数：', len(TotalPosts))
    # 拿到该标签下的对应的数据
    for item in TotalPosts:
        # 帖子标题
        title = item.xpath('.//a[@class="j_th_tit "]/text()')[0]
        print('帖子标题：', title)
        # 帖子地址
        url = 'http://tieba.baidu.com' + item.xpath('.//a[@class="j_th_tit "]/@href')[0]
        print('帖子地址：', url)
        # 帖子回复数
        reply_num = item.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
        print('帖子回复数：', reply_num)
        # 帖子作者
        author = item.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')
        # 如果作者不存在
        if len(author) > 0:
            author = author[0]

        else:
            author = '无'
        print('帖子作者：', author)
        # 最后一个回复的人
        reply = item.xpath('.//span[@class="tb_icon_author_rely j_replyer"]/a/text()')
        if len(reply) > 0:
            reply = reply[0]
        else:
            reply = '无'
        print('最后一个回复的人：', reply)
        # 回复时间
        reply_time = item.xpath('.//span[@class="threadlist_reply_date pull_right j_reply_data"]/text()')
        if len(reply_time) > 0:
            reply_time = reply_time[0].replace('\n', '').strip()
        else:
            reply_time = '无'
        print('回复时间：', reply_time)
        # 分割线
        print('='*120)

        """
            3.数据的存储
        """
        # 方式1.存为 txt 格式
        txt_filename = './data/' + name + '吧' + '.txt'
        with open(txt_filename, 'a', encoding='utf-8') as f:
            f.write(title+','+url+','+reply_num+','+author+','+reply+','+reply_time+'\n')

        # 方式2.存为 csv 格式
        csv_filename = './data/' + name + '吧' + '.csv'
        with codecs.open(csv_filename, 'a', encoding='utf-8') as f:
            wr = csv.writer(f)
            wr.writerow([title, url, reply_num, author, reply, reply_time])
