# -*- coding: utf-8 -*-
from crawler_queue import crawler_queue
seeds = ["javascript:openimagewindow('https://www.pcmag.com/image_popup/0,1740,iid=559369,00.asp', '810', '456')",'https://sea.pcmag.com/smartphones/73/the-best-phones']
obj = crawler_queue(seeds, 'test.json')
obj.run()