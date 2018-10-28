# -*- coding: utf-8 -*-
from crawler_queue import crawler_queue

def get_seed(filename):
    try:
        with open(filename, 'r') as f:
         return [x.strip() for x in f.readlines()]
    except:
        return []

filename = 'seed.txt'
seeds = get_seed(filename)
obj = crawler_queue(seeds, 'test.json')
obj.run()
