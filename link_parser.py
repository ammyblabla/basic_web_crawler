# -*- coding: utf-8 -*-
from urllib.parse import urljoin
from urllib.parse import urlparse

def link_parser(base_url, raw_html):
    urls = []
    pattern_start = '<a href="'; pattern_end = '"'
    index = 0; length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            link = raw_html[start:end]
            link = urljoin(base_url, link)
            if len(link) > 0:
                if link[-1] == '/':
                    link = link[:-1]
                if (link not in urls) and (filter(link)):
                    urls.append(link)
            index = end
        else: 
            break
    # print(urls)
    return urls

def filter(url):
    o = urlparse(url)
    base_url = o.netloc
    if '.php' in url:
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
        if filetype != 'html' or filetype != 'htm':
           return False
    return True

def is_html(url):
    o = urlparse(url)
    last_path = o.path.split('/')[-1]
    if '.' in last_path:
        filetype = last_path.split('.')[-1]
        if filetype == 'html' or filetype == 'htm':
            return True
    return False