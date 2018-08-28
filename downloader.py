import requests

headers = {
    'User-Agent': 'Natnaree Asavaseri User Agent 1.0',
    'From': 'natnaree.as@ku.th'
}

def get_page(url):
    global headers
    text = ''
    try:
        print(f'GETTING {url}')
        r = requests.get(url, headers=headers, timeout = 2)
        text = r.text
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        print('GET PAGE ERROR!')
    return text.lower()

# def save_page(url, text):
#     o = urlparse(url)
