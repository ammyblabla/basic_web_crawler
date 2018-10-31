# -*- coding: utf-8 -*-
from downloader import get_page
from save_page import save_page,clean_text
from link_parser import link_parser, is_html
import tldextract
from  robot_sitemaps import robot_sitemaps
import codecs
from filter_method import is_english, is_url, content_filter

class crawler_queue():
    def __init__(self,seed_url, result_filename):
        self.frontier_q = list(set(seed_url +  get_exist_link('frontier_q.txt')))
        self.html_page = get_exist_link('lists_html.txt')
        self.visited_q  = list(set(get_exist_link('visited_q.txt') + self.html_page))
        self.seed_domain_list = get_domain_list(seed_url)
        self.robot_obj = robot_sitemaps()
        self.filename = result_filename
    # self.frontier_q = seed_url
    # self.visited_q = []
    # self.html_page = []
    # while len(self.frontier_q) > 0:


    def run(self):
        while len(self.html_page) < 10000 and len(self.frontier_q) > 0:
            # print(type(self.frontier_q))
            # print(type(self.frontier_q[0]))
            current_url = self.frontier_q[0]
            self.frontier_q = self.frontier_q[1:]
            text = ''
            if (not (self.robot_obj.robot_filter(current_url))):
                self.visited_q.append(current_url)
                continue
            res = None
            try:
                res = get_page(current_url)
            except:
                print('GET PAGE ERROR IN QUEUE')
                continue

            text = res['text']
            self.visited_q.append(current_url)
            if (res['status_code'] != 200) or (res['result'] == 0):
                print('REQUEST NOT SUCCESSFUL')
                continue
            if res['url'] != current_url:
                print('REDIRECT')
                if res['url'] in self.visited_q:
                    continue
                if res['url'] in self.frontier_q:
                    self.frontier_q.remove(res['url'])

            if not content_filter(clean_text(text)['text']):
                print('CONTENT ERROR')
                continue
            # else:
            #     print(current_url)

            # if is_html(current_url):
            try:
                save_page(res, self.filename, write_file=True)
                # print('SAVE PAGE')
            except:
                print('SAVE PAGE ERROR')
                continue

            self.html_page.append(res['url'])
            self.html_page = list(set(self.html_page))
            # self.robot_obj.write_file(text=current_url, file='lists_html.txt', permission='a')
            write_list(self.html_page,'lists_html.txt')
            print('ADD IN HTML LIST')

            try:
                extracted_links = link_parser(res['url'], text)
                for link in extracted_links:
                    # print(link)
                    if (get_domain(link) in self.seed_domain_list) and is_url(link) and is_english(text):
                        if (link not in self.frontier_q) and (link not in self.visited_q):
                            # print(link)
                            self.frontier_q.append(link)
                    else:
                        self.visited_q.append(link)

            except:
                print('EXTRACT LINK ERROR')
                pass
            # print(text)
            self.visited_q = list(set(self.visited_q))
            self.frontier_q = list(set(self.frontier_q))

            print(f'visited queue length {len(self.visited_q)}')
            print(f'frontier queue length {len(self.frontier_q)}')
            print(f'html list {len(self.html_page)}')
                # break
            # print(self.frontier_q) 
            write_list(self.visited_q,'visited_q.txt')
            write_list(self.frontier_q,'frontier_q.txt')
        print('finish')
        return self.frontier_q

def get_exist_link(filename):
    try:
        f = codecs.open(filename, 'r', 'utf-8')
        return [x.strip() for x in f.readlines()]
    except:
        return []

def write_file(text, file, permission='a'):
    f = codecs.open(file, permission, 'utf-8')
    f.write(text)
    f.write('\n')
    f.close()

def write_list(lines,filename):
    f = codecs.open(filename, 'w', 'utf-8')
    for line in lines:
        f.write(line+'\n')
    f.close()

def get_domain(url):
    ext = tldextract.extract(url)
    return '.'.join(ext[1:])

def get_domain_list(urls):
    domains = []
    for url in urls:
        domains.append(get_domain(url))
    # print(domains)
    return domains