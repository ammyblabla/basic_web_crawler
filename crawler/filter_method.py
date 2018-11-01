from bs4 import BeautifulSoup
from urllib.parse import urlparse


def is_english(text):
    soup = BeautifulSoup(text, 'html.parser')
    attrs = soup.html.attrs
    res = True
    if 'lang' in attrs:
        lang = soup.html.attrs['lang']
        if not 'en' in lang:
            return False
    return res

def is_url(url):
  if '?' in url:
    return False
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

def content_filter(text):
  if 'samsung' in text:
    if ('mobile' in text) or ('phone' in text):
      return True 
  return False