from lxml import etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# # 将字符串解析为 html 文档
# html = etree.HTML(text)
# # <class 'lxml.etree._Element'>
# print(type(html))
# # 按字符串序列化HTML文档，结果将最后一个 li 标签补全，还自动添加了html、body标签
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# ————————————————————————————————————————————————————————————————————————————————————
# 也可以直接引入文本文件进行解析，结果与上边多了一个 DOCTYPE的声明
# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# ————————————————————————————————————————————————————————————————————————————————————
"""
    所有节点
"""
html = etree.parse('./test.html', etree.HTMLParser())
# xpath
result = html.xpath('//*')
print(result)