#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
from pymongo import MongoClient
from urllib.parse import urlencode


client = MongoClient()
session = requests.Session()

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
}

def get_param(max_behot_time):
    local_url = "http://127.0.0.1:3000/pic?param=get_signature(%s)"%max_behot_time
    res = requests.get(local_url)
    return res.json()

# param = get_param(0)

def parse_one(max_behot_time):
    param = get_param(max_behot_time)
    param['category'] = "组图"
    param['utm_source'] = "toutiao"
    param['max_behot_time'] = max_behot_time
    print(param)
    url = "https://www.toutiao.com/api/pc/feed/"
    print("url:",url + "?" + urlencode(param))
    response = requests.get(url,headers=headers,params=param)
    print(response.text)
    next_max_behot_time = response.json()['next']['max_behot_time']
    data = response.json()['data']
    item = []
    for each in data:
        data = {}
        # pprint(each)
        title = each['title']
        image_url = each['image_url']
        print(image_url)
        data['title'] = title
        data['image_url'] = image_url
        print(f"title:{title}")
        item.append(data)
    return item,next_max_behot_time

def run():
    '''循环获取几页的数据进行尝试'''
    max_behot_time = 0
    collection = client.toutiao.pic  # 连接集合pic
    i = 1
    while i< 50:
        item,max_behot_time = parse_one(max_behot_time)
        print("item:",item)
        collection.insert_many(item)
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    run()