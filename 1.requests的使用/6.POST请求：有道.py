import requests

if __name__ == '__main__':
    #
    # http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    # 这里需要去掉 _o,代表初次查词
    # http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule
    request_URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 定义一个字典，存储表单数据
    form_Data = {}
    form_Data['i'] = 'computer'  # 要翻译的词
    form_Data['from'] = 'AUTO'
    form_Data['to'] = 'AUTO'
    form_Data['smartresult'] = 'dict'
    form_Data['client'] = 'client'
    form_Data['salt'] = '15674318214216'
    form_Data['sign'] = '8022aa5a73744b84afb542c235e44e75'
    form_Data['doctype'] = 'json'
    form_Data['keyfrom'] = 'fanyi.web'
    form_Data['action'] = 'FY_BY_REALTlME'
    form_Data['version'] = '2.1'

    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    r = requests.post(request_URL, data=form_Data, headers=head)
    print(r)
    print(r.text)
    # 翻译结果
    translate_results = r.json()
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print('翻译的结果是：%s' % translate_results)
