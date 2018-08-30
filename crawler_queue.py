# -*- coding: utf-8 -*-
from downloader import get_page, save_page
from link_parser import link_parser, is_html
from robot_sitemaps import robot_filter, write_file

def crawler_queue(seed_url):
    frontier_q = seed_url
    visited_q = []
    html_page = []
    robots = []
    # while len(frontier_q) > 0:
    while len(html_page) < 10000 and len(frontier_q) > 0:
        current_url = frontier_q[0]
        frontier_q = frontier_q[1:]
        text = ''
        if not robot_filter(current_url):
            visited_q.append(current_url)
            continue

        res = get_page(current_url)
        text = res['text']
        if (res['status_code'] != 200) or (res['result'] == 0):
            visited_q.append(current_url)
            continue

        if is_html(current_url):
            html_page.append(current_url)
            save_page(current_url, text)
            write_file(text=current_url, file='lists_html.txt', permission='a')

        extracted_links = link_parser(current_url, text)
        
        # print(text)
        visited_q.append(current_url)

        for link in extracted_links:
            if link not in frontier_q and link not in visited_q:
                # print(link)
                frontier_q.append(link)
        print(f'visited queue length {len(visited_q)}')
        print(f'frontier queue length {len(frontier_q)}')
        print(f'html list {len(html_page)}')
        # break
    # print(frontier_q) 
    return frontier_q