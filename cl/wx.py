# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 22:07
# @Author  : cmsll
# @Site    : 
# @File    : wx.py
# @Software: PyCharm

import requests
import os
from bs4 import BeautifulSoup
import common
import re


# def get_artical_links(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup('h3')
#     # print(links)
#     artical_links = []
#     regex = re.compile('htm_data')
#     for link in links:
#         print(link)
#         artical_link = link.get('href')
#         print(artical_link)
#         # print(re.match(regex, artical_link))
#         # if re.match(html, regex):
#         #     artical_links.append(artical_link)
#     print(artical_links)
def get_artical_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    regex = re.compile('htm_data')
    artical_links = []
    site_description_links = ['htm_data/20/0805/131469.html', 'htm_data/20/0810/183193.html', 'htm_data/20/1711/932276.html']
    for child in soup.descendants:
        if child.name == 'h3':
            # print(child.a)
            link = child.a.get('href')
            if re.match(regex, link) and link not in site_description_links:
                # print(link)
                artical_link = 'http://cl.b8y.xyz/'+ link
                artical_links.append(artical_link)
    print(artical_links)
    return artical_links




html = common.get_html_text('http://cl.b8y.xyz/thread0806.php?fid=20')
get_artical_links(html)