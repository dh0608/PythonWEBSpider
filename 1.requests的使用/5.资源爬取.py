import requests, chardet

"""
    图片爬取
"""

# r = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568030620&di=5e27c69449e0ff6b6a8565e989ff0078&imgtype=jpg&er=1&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20190817%2Ff2459dfc9726427ab7439042edeb360f.jpeg')
# with open('./images/nezha.jpg', 'wb') as f:
#     f.write(r.content)

"""
    视频爬取
"""

# def download_file(url, path):
#     # r = requests.get(url, stream=True)
#     with requests.get(url, stream=True) as r:
#         chunk_size = 1024
#         # content_size = int(r.headers['content-length'])
#         print('下载开始......')
#         with open(path, "wb") as f:
#             for chunk in r.iter_content(chunk_size=chunk_size):
#                 f.write(chunk)
#     print('下载结束.....')
#
#
# if __name__ == '__main__':
#     url = 'https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo-transcode/51722773_98a3bb47a51fef46145630154f007ddc_0.mp4'
#     path = './videos/v.mp4'
#     download_file(url, path)

"""
    网页爬取
"""

# 爬取贴吧
url = 'http://tieba.com/f'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
name = input('请输入贴吧名称：')
start_page = int(input('请输入起始的页码：'))
end_page = int(input('请输入结束的页码：'))
for page in range(start_page, end_page + 1):
    pn = (page - 1) * 50
    params = {
        'kw': name,
        'ie': 'utf-8',
        'pn': pn
    }
    r = requests.get(url, params=params, headers=headers)
    file = r.text
    print(page)
    filename = './html/name+第%s页.html' % page
    with open(filename, 'w', encoding='utf8') as f:
        f.write(file)

# def Crawl_web_pages(url, path):
#     # print(url.content)
#     # print(url.apparent_encoding)
#
#     with open(path, 'wb') as f:
#         f.write(url.text.encode('utf8'))
#
#
# Crawl_web_pages(url=requests.get('https://www.qq.com/'), path='./html/qq.html')
# Crawl_web_pages(url=requests.get('http://kan.sogou.com/dongman/'),
#                 path='./html/dongman.html')
# Crawl_web_pages(url=requests.get('http://www.4399.com/?haoqqdh'), path='./html/4399.html')
# Crawl_web_pages(url=requests.get('http://health.sohu.com/?spm=smpc.home.top-nav.24.1550453761461Q0shOpW'),
#                 path='./html/sohuhealth.html')
