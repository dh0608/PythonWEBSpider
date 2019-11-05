"""
    案例：脉脉app职言信息的爬取
    爬取职言作者，标题，头像链接，发表时间，评论数，点赞数
    https://open.taou.com/maimai/gossip/v3/feed?u=228797653&access_token=1.8b63d56138579efa4933981b1fa0abe3&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=OPPO%20OPPO%20R11&imei=866174010542252&udid=bac66bc4-99eb-49a6-bad5-41ca5e0fca28&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=f9f9d9f3-aa45-41ae-9ab5-2acee097dc66&session_uuid=60a938f4-b1fb-4982-b42c-4b37d92de0c3&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3Df6fb051f-7819-45f7-92eb-a7beaf10c6b6%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&src_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.react.MaiMaiReactActivity%26uuid%3D757cdead-8b4e-426c-900e-65f66e14ccbb%26url%3Dtaoumaimai%253A%252F%252Frct%253Fcomponent%253DEditWorkExp%2526firstWorkExp%253D1%2526%253D%2526guideProgresses%253D%2526showClose%253D1%2526useWhiteStyle%253Dtrue%2526_inWorkflow_%253D1%2526visitors%253D%2526guideTitle%253D%2525E4%2525BD%2525A0%2525E5%25259C%2525A8%2525E5%25258C%252597%2525E4%2525BA%2525AC%2525E5%2525A5%252587%2525E9%252585%2525B7%2525E5%25258A%2525A8%2525E5%25258A%25259B%2525E4%2525BF%2525A1%2525E6%252581%2525AF%2525E6%25258A%252580%2525E6%25259C%2525AF%2525E6%25259C%252589%2525E9%252599%252590%2525E5%252585%2525AC%2525E5%25258F%2525B8%2525E7%25259A%252584%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525E6%252597%2525B6%2525E9%252597%2525B4%2525E6%252598%2525AF%2525EF%2525BC%25259F%2526id%253D61676508%2526subTitle%253D%2525E5%2525AE%25258C%2525E5%252596%252584%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525E7%2525BB%25258F%2525E5%25258E%252586%2525EF%2525BC%25258C%2525E6%25258A%252593%2525E4%2525BD%25258F%2525E6%2525BD%25259C%2525E5%25259C%2525A8%2525E6%25259C%2525BA%2525E9%252581%252587%2526showBottomGuideFlowSkip%253Dtrue%2526title%253D%2525E4%2525B8%252581%2525E8%2525B1%2525AA%2525EF%2525BC%25258C%2525E6%2525AC%2525A2%2525E8%2525BF%25258E%2525E5%25259B%25259E%2525E6%25259D%2525A5%2525EF%2525BC%252581%2526isNotShowCloseConfirm%253Dnull%2526scene%253Dguide%2526isWorkExpDescOptional%253Dtrue%2526profile_abtest%253D%25257B%252522visitorsMoreThenThree%252522%25253Anull%25257D%2526editable%253Dtrue&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.gossip.fragment.GossipFragmentRefactor%26uuid%3Dcb33fdc2-8fd2-48f6-b860-85c33619c4f2&action=first_load&page=0
    author = name
    text =
    avatar=http://i9.taou.com/maimai/p/aurl/v3/avatar_other.png
    hash=1568768663.09006955277
    cmts=41
    likes=65
"""
import requests
from lxml import html
import time
import json
etree = html.etree


url = 'https://open.taou.com/maimai/gossip/v3/feed?u=228797653&access_token=1.8b63d56138579efa4933981b1fa0abe3&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=OPPO%20OPPO%20R11&imei=866174010542252&udid=bac66bc4-99eb-49a6-bad5-41ca5e0fca28&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=f9f9d9f3-aa45-41ae-9ab5-2acee097dc66&session_uuid=60a938f4-b1fb-4982-b42c-4b37d92de0c3&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3Df6fb051f-7819-45f7-92eb-a7beaf10c6b6%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&src_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.react.MaiMaiReactActivity%26uuid%3D757cdead-8b4e-426c-900e-65f66e14ccbb%26url%3Dtaoumaimai%253A%252F%252Frct%253Fcomponent%253DEditWorkExp%2526firstWorkExp%253D1%2526%253D%2526guideProgresses%253D%2526showClose%253D1%2526useWhiteStyle%253Dtrue%2526_inWorkflow_%253D1%2526visitors%253D%2526guideTitle%253D%2525E4%2525BD%2525A0%2525E5%25259C%2525A8%2525E5%25258C%252597%2525E4%2525BA%2525AC%2525E5%2525A5%252587%2525E9%252585%2525B7%2525E5%25258A%2525A8%2525E5%25258A%25259B%2525E4%2525BF%2525A1%2525E6%252581%2525AF%2525E6%25258A%252580%2525E6%25259C%2525AF%2525E6%25259C%252589%2525E9%252599%252590%2525E5%252585%2525AC%2525E5%25258F%2525B8%2525E7%25259A%252584%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525E6%252597%2525B6%2525E9%252597%2525B4%2525E6%252598%2525AF%2525EF%2525BC%25259F%2526id%253D61676508%2526subTitle%253D%2525E5%2525AE%25258C%2525E5%252596%252584%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525E7%2525BB%25258F%2525E5%25258E%252586%2525EF%2525BC%25258C%2525E6%25258A%252593%2525E4%2525BD%25258F%2525E6%2525BD%25259C%2525E5%25259C%2525A8%2525E6%25259C%2525BA%2525E9%252581%252587%2526showBottomGuideFlowSkip%253Dtrue%2526title%253D%2525E4%2525B8%252581%2525E8%2525B1%2525AA%2525EF%2525BC%25258C%2525E6%2525AC%2525A2%2525E8%2525BF%25258E%2525E5%25259B%25259E%2525E6%25259D%2525A5%2525EF%2525BC%252581%2526isNotShowCloseConfirm%253Dnull%2526scene%253Dguide%2526isWorkExpDescOptional%253Dtrue%2526profile_abtest%253D%25257B%252522visitorsMoreThenThree%252522%25253Anull%25257D%2526editable%253Dtrue&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.gossip.fragment.GossipFragmentRefactor%26uuid%3Dcb33fdc2-8fd2-48f6-b860-85c33619c4f2&action=first_load&page=0'
headers = {'User-Agent': '{samsung SM-G955N} [Android 4.4.2/19]/MaiMai 5.0.16(10018)'}
# requests提示警告InsecureRequestWarning,加上这一句就不会报错了
requests.packages.urllib3.disable_warnings()
r = requests.get(url, verify=False, headers=headers).json()
# print(r.json())
# print(r['data'])
ls = r['data']
for item in ls:
    # print(item)
    author = item['author']
    print(f'作者:{author}')

    text = item['text'].strip().replace('\n', '')
    print(f'标题:{text}')

    text_url = item['share_url'].strip()
    print(f'头像链接:{text_url}')

    # 1568979429 725996501
    # 1568680096 299903950
    pub_time = item['hash']
    if pub_time.isdigit():
        pub_time = pub_time[:10]
        timeArray = time.localtime(int(pub_time))
        pub_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    else:
        pub_time = '空'

    print(f'发表时间：{pub_time}')

    comments = item['cmts']
    print(f'评论数:{comments}')

    good = item['likes']
    print(f'点赞数:{good}')

    print('=' * 120)
