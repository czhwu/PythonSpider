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


# def get_article_links(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup('h3')
#     # print(links)
#     article_links = []
#     regex = re.compile('htm_data')
#     for link in links:
#         print(link)
#         article_link = link.get('href')
#         print(article_link)
#         # print(re.match(regex, article_link))
#         # if re.match(html, regex):
#         #     article_links.append(article_link)
#     print(article_links)
def get_article_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    regex = re.compile('htm_data')
    article_links = []
    site_description_links = ['htm_data/20/0805/131469.html', 'htm_data/20/0810/183193.html', 'htm_data/20/1711/932276.html']
    for child in soup.descendants:
        if child.name == 'h3':
            # print(child.a)
            link = child.a.get('href')
            if re.match(regex, link) and link not in site_description_links:
                # print(link)
                article_link = 'http://cl.b8y.xyz/'+ link
                article_links.append(article_link)
    # print(article_links)
    return article_links


def get_title_content(text):
    # global title
    soup = BeautifulSoup(text, 'html.parser')
    for child in soup.descendants:
        if child.name == 'h4':
            title = child.string
            # print(title)
    ss = soup('div', class_='tpc_content do_not_catch')
    contents = []
    for s in ss:
        if len(s)>100:
            # print(type(s))
            content = re.sub('<div class="tpc_content do_not_catch">|</div>', '', str(s))
            # print(content)
            contents.append(content)

    # print(content)
    return [title, contents]


def save_article(text):
    root = 'g://text//'
    (title, contents) = get_title_content(text)
    # print(title, contents)
    if title:
        path = root + title + '.txt'
        print(path)
        if not os.path.exists(root):
            os.makedirs(root)
        if not os.path.exists(path):
            print('creating path...')
            with open(path, 'wb') as f:
                for content in contents:
                    f.write(bytearray(content, 'utf8'))
                    f.close()
                    print(path + '.txt has saved sucessfully!')
        else:
            print(title+'.txt has already exist.')
    else:
        path = root + 'black.txt'
        print(path)
        if not os.path.exists(root):
            os.makedirs(root)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(bytearray('', 'utf8'))
                f.close()
        # pass


html = common.get_html_text('http://cl.b8y.xyz/thread0806.php?fid=21')
article_links = get_article_links(html)
for article_link in article_links:
    print(article_link)
    html_sub = common.get_html_text(article_link)
    # (title, contents) = get_title_content(html_sub)
    # print(title)
    # for content in contents:
    #     print(content)
    #     save_article(content)
    save_article(html_sub)
