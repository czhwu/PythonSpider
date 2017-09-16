# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 22:29
# @Author  :
# @Site    :
# @File    : qz.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import os
import re
import datetime
import requests


def get_html_text(url):
    """

    :param url:
    :return:
    """
    kv = {'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'}
    try:
        r = requests.get(url=url, headers=kv, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


# '	<h3><a href="htm_data/16/1709/2645749.html" target="_blank" id="">[原创]</a></h3>  '
def get_item_url(html):
    # 做汤
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    # 获取页面中'href="htm_data****"'的链接
    aa = soup('a',  attrs={'href': re.compile('htm_data')})
    # 提取链接地址并放入列表links中
    links = []
    for a in aa:
        link = 'http://cl.b8y.xyz/' + a.get('href')
        links.append(link)
    # print(links)
    return links


# '<input src="http://tu303.com/u/20170915/1105752.jpg" type="image" />
def get_image_url(html):
    """
    获取页面中符合要求的图片的地址，并返回地址列表
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    inputs = soup('input', attrs={'type': 'image'})
    image_links = []
    for input in inputs:
        image_link = input.get('src')
        image_links.append(image_link)
    # print(image_links)
    return image_links


def save_image(image_url):
    """
    保存图片到指定位置
    :param image_url:
    :return:
    """
    # 获取图片的二进制数据，方便下一步的保存
    content = requests.get(image_url, timeout=30).content
    # 设定存储路径，并判断是否存在
    root = 'g://image//'+ str(datetime.date.today()) + '//'
    if not os.path.exists(root):
        os.makedirs(root)
    # 设定文件名称，判断是否存在并保存文件
    path = root + image_url.split('/')[-1]
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            f.close()
        print(path + ' saved successfully.')
    else:
        print(path + ' has already exists!')


url = 'http://cl.b8y.xyz/thread0806.php?fid=16&search=&page=2'
html = get_html_text(url)
# print(html)
links = get_item_url(html)
for link in links:
    text = get_html_text(link)
    image_links = get_image_url(text)
    for image_link in image_links:
        save_image(image_link)


