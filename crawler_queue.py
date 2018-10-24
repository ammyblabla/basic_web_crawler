# -*- coding: utf-8 -*-
from downloader import get_page, save_page
from link_parser import link_parser, is_html
# from robot_sitemaps import robot_filter, write_file
from  robot_sitemaps import robot_sitemaps

class crawler_queue():
    def __init__(self,seed_url):
        self.frontier_q = seed_url
        self.html_page = []
        self.visited_q  = self.html_page
        self.robot_obj = robot_sitemaps()
    # self.frontier_q = seed_url
    # self.visited_q = []
    # self.html_page = []
    # while len(self.frontier_q) > 0:
    def run(self):
        while len(self.html_page) < 10000 and len(self.frontier_q) > 0:
            current_url = self.frontier_q[0]
            self.frontier_q = self.frontier_q[1:]
            text = ''
            if not (self.robot_obj.robot_filter(current_url)):
                self.visited_q.append(current_url)
                continue

            res = get_page(current_url)
            text = res['text']
            self.visited_q.append(current_url)
            if (res['status_code'] != 200) or (res['result'] == 0):
                continue

            if is_html(current_url):
                self.html_page.append(current_url)
                try: 
                    save_page(current_url, text)
                    self.robot_obj.write_file(text=current_url, file='lists_html.txt', permission='a')
                except:
                    pass
            try:
                extracted_links = link_parser(current_url, text)
                for link in extracted_links:
                    if link not in self.frontier_q and link not in self.visited_q:
                        # print(link)
                        self.frontier_q.append(link)
            except:
                pass
            # print(text)

            print(f'visited queue length {len(self.visited_q)}')
            print(f'frontier queue length {len(self.frontier_q)}')
            print(f'html list {len(self.html_page)}')
            # break
        # print(self.frontier_q) 
        print('finish')
        return self.frontier_q