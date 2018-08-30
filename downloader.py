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
        r = requests.get(url, headers=headers, timeout = 2)
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
        'text':text.lower(),
        'status_code': status_code,
        'result' : res
    }

def save_page(url, text):
    url_lists = url.split('/')
    for i in range(len(url_lists)):
        url_lists[i] = url_lists[i].replace(':','-').replace('?','-')
    filename =  url_lists[-1]
    dir =  'html/' + '/'.join(url_lists[2:-1])
    # print(f'writing {filename}')
    # print(dir)
    # print(filename)
    # print(dir)
    fullname = dir + '/' + filename
    # print(fullname)
    Path(dir).mkdir(parents=True, exist_ok=True) 
    Path(fullname).touch()
    f = codecs.open(fullname, 'w','utf-8')
    f.write(text)
    f.close()