# -*- coding: utf-8 -*-

from downloader import get_page 
from link_parser import *
from robot_sitemaps import *
# from downloader import save_page

url = 'http://www.ku.ac.th'
print(find_sitemap(url))