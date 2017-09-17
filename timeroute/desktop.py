# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 23:48
# @Author  : cmsll
# @Site    : 
# @File    : desktop.py
# @Software: PyCharm


import requests
import os
from bs4 import BeautifulSoup
import common


def get_image_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup('img', class_='card-img-top round-0')
    # print(imgs)
    image_links = []
    for img in imgs:
        image_link = img.get('source')
        image_links.append(image_link)
    return image_links


def save_image(image_link):
    content = requests.get(image_link, timeout=10).content
    root = 'g://img//timeroute//'
    if not os.path.exists(root):
        os.makedirs(root)
    path = root + image_link.split('/')[-1]
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            f.close()
        print(path + ' saved sucessfully.')
    else:
        print(path + ' has already exist!')

for i in range(0, 805):
    url = 'http://timeroute.cn/desktop/page/%d' % i
    print(url)
    html = common.get_html_text(url)
    image_links = get_image_links(html)
    for image_link in image_links:
        save_image(image_link)