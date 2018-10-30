# -*- coding: utf-8 -*-
import requests
from pathlib import Path
import codecs
from proxy_request import proxy

class downloader():
    def __init__(self):
        self.proxy_obj = proxy()

    def get_page(self,url):
        text = ''
        res = 0
        r = None
        status_code = None
        real_url = url
        try:
            print(f'GETTING {url}')
            # r = requests.get(url, headers=headers, timeout = 2)
            r = self.proxy_obj.request_page(url)
            text = r.text
            real_url = r.url
            res = 1
            status_code = r.status_code
            if r.status_code != 200:
                print('PAGE HAS PROBLEM!', status_code)
        except(KeyboardInterrupt, SystemExit):
            raise
        except Exception as e:
            # print(e)
            print('GET PAGE ERROR!')
        
        return {
            'url': real_url,
            'text':text.lower(),
            'status_code': status_code,
            'result' : res,
        }