# -*- coding: utf-8 -*-
from downloader import get_page
from save_page import save_page
from link_parser import link_parser, is_html
import tldextract
from bs4 import BeautifulSoup
from  robot_sitemaps import robot_sitemaps
from urllib.parse import urlparse
import codecs

class crawler_queue():
    def __init__(self,seed_url, result_filename):
        self.frontier_q = seed_url +  get_exist_link('frontier_q.txt')
        self.html_page = get_exist_link('lists_html.txt')
        self.visited_q  = get_exist_link('visited_q.txt')
        self.seed_domain_list = get_domain_list(seed_url)
        self.robot_obj = robot_sitemaps()
        self.filename = result_filename
    # self.frontier_q = seed_url
    # self.visited_q = []
    # self.html_page = []
    # while len(self.frontier_q) > 0:


    def run(self):
        while len(self.html_page) < 10000 and len(self.frontier_q) > 0:
            current_url = self.frontier_q[0]
            self.frontier_q = self.frontier_q[1:]
            text = ''
            if (not (self.robot_obj.robot_filter(current_url))):
                self.visited_q.append(current_url)
                continue

            res = get_page(current_url)
            text = res['text']
            self.visited_q.append(current_url)
            if (res['status_code'] != 200) or (res['result'] == 0):
                continue

            # if is_html(current_url):
            self.html_page.append(current_url)
            save_page(res, self.filename, write_file=True)
            # self.robot_obj.write_file(text=current_url, file='lists_html.txt', permission='a')
            write_list(self.html_page,'lists_html.txt')

            try:
                extracted_links = link_parser(current_url, text)
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
    print(domains)
    return domains

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

def is_english(text):
    soup = BeautifulSoup(text, 'html.parser')
    attrs = soup.html.attrs
    res = True
    if 'lang' in attrs:
        lang = soup.html.attrs['lang']
        if lang != 'en':
            return True
    # print('is eng', res)
    return res
