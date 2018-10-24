# -*- coding: utf-8 -*-
from urllib.parse import urljoin
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def link_parser(base_url, raw_html):
    urls = []
    soup = BeautifulSoup(raw_html, 'lxml')
    links = soup.findAll('a')
    for link in links:
        try:
            link = link.attrs['href']
            link = urljoin(base_url, link)
            if len(link) > 0:
                if link[-1] == '/':
                    link = link[:-1]
                if (link not in urls) and (filter(link)):
                    # print(link)
                    urls.append(link)
        except:
            continue
        # print(link)
    return urls

def filter(url):
    o = urlparse(url)
    base_url = o.netloc
    if ('.php' in url) or ('pdf' in url):
        return False
    if 'ku.ac.th' not in base_url:
        return False
    if not file_type_filter(url):
        return False
    url_split = url.split('/')
    if '#' in url_split[-1]:
        return False
    return True

def file_type_filter(url):
    o = urlparse(url)
    last_path = o.path.split('/')[-1]
    # print(last_path)
    if '.' in last_path:
        filetype = last_path.split('.')[-1]
        # print(filetype)
        if filetype != 'html' and filetype != 'htm':
           return False
    return True

def is_html(url):
    # print(url)
    delimeter = None
    if '/' in url:
        delimeter = '/'
    elif '\\' in url:
        delimeter = '\\'
    last_path = url.split(delimeter)[-1]
    # print(last_path)
    if '.' in last_path:
        filetype = last_path.split('.')[-1]
        if filetype == 'html' or filetype == 'htm':
            return True
    return False