# -*- coding: utf-8 -*-
import sys
import requests
import os
import json
import base64
import re
url = 'https://ucmp.sf-express.com/cx-wechat-query/query/waybill/queryWayBillByWaybillNo'
headers = {
    "Cookie": 'HSESSION=3686bc32cc4c4039b98f7db55a9e3af2',
    "Host": "ucmp.sf-express.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400",
    }
json_data = {"countryCode":"CN","langCode":"sc","mediaCode":"WEIXIN","systemCode":"ccsp","businessCode":"","waybillNos":["609194905912"]}
s1=requests.post(url, json=json_data, headers=headers)
print(s1.status_code)
print(s1.encoding)
print (s1.text)
with open('result.txt', 'a+', encoding='utf-8') as f:
    f.write(s1.text)
