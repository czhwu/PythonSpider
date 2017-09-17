# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 22:29
# @Author  :
# @Site    : 
# @File    : lists.py
# @Software: PyCharm


import os
import re
import requests
from bs4 import BeautifulSoup

# faild, 使用JavaScript
def get_html_text(keyword):
    try:
        r = requests.get('https://s.taobao.com/search?', params={'q': keyword})
        r.raise_for_status()
        r.encoding  = r.apparent_encoding
        return r.text
    except:
        return ''


def get_item(html):
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    div_item_list = soup.find_all(class_='logo')
    print(div_item_list)

html = get_html_text('phone')
get_item(html)