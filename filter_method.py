from bs4 import BeautifulSoup
from urllib.parse import urlparse


def is_english(text):
    soup = BeautifulSoup(text, 'html.parser')
    attrs = soup.html.attrs
    res = True
    if 'lang' in attrs:
        lang = soup.html.attrs['lang']
        if lang != 'en':
            return False
    # print('is eng', res)
    return res

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False