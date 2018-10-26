# -*- coding: utf-8 -*-
import requests
from pathlib import Path
import codecs


headers = {
    'User-Agent': 'Natnaree Asavaseri User Agent 1.0',
    'From': 'natnaree.as@ku.th'
}

def get_page(url):
    global headers
    text = ''
    res = 0
    r = None
    status_code = None
    try:
        print(f'GETTING {url}')
        r = requests.get(url, headers=headers, timeout = 2, allow_redirects=False)
        text = r.text
        res = 1
        status_code = r.status_code
        if r.status_code != 200:
            print('PAGE HAS PROBLEM!', status_code)
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        print('GET PAGE ERROR!')
    
    return {
        'url': url,
        'text':text.lower(),
        'status_code': status_code,
        'result' : res
    }