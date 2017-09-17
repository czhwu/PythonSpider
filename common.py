# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 23:56
# @Author  : cmsll
# @Site    : 
# @File    : common.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    kv = {'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'}
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''