# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from downloader import get_page 
from link_parser import *
from robot_sitemaps import *
import requests
import re
from downloader import *
import codecs
# from downloader import save_page

# url = 'http://www.cyberlab.lh1.ku.ac.th/index.html'
# # print(is_html(url))
# # try:
# r = requests.get(url, headers=headers, timeout = 2)
# print(r.status_code)
#     # text = r.text
#     # print(save_page(url, text))
# # except:
# #     raise

f = codecs.open('lists_html.txt', 'r', 'utf-8')
f2 = codecs.open('lists_html_new.txt', 'w', 'utf-8')

for line in f:
    # print(line)
    f2.write(f'"{line.strip()}",')
    f2.write('\n')
f.close()
f2.close()