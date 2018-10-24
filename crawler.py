# -*- coding: utf-8 -*-
from crawler_queue import crawler_queue
seeds = ['https://www.ku.ac.th/web2012/']
obj = crawler_queue(seeds)
obj.run()