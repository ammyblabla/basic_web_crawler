# -*- coding: utf-8 -*-

def link_parser(raw_html):
    urls = []
    pattern_start = '<a href="'; pattern_end = '"'
    index = 0; length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            link = raw_html[start:end]
            if len(link) > 0:
                if link not in urls:
                    urls.append(link)
            index = end
        else: 
            break
    return urls
