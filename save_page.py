from pathlib import Path
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract
import re
# import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


def save_page(input, filename, write_file=True):
   html_doc = input['text']
   url = input['url']
   # print(f'save {url}')
   soup = BeautifulSoup(html_doc, 'html.parser')
   [s.extract() for s in soup('script')]
   [s.extract() for s in soup('style')]
   text = soup.text.strip().replace('\xa0', ' ').replace('\n',' ').replace('\t',' ').replace('\r',' ')
   text = re.sub(r"<!--(.|\s|\n)*?-->", "", text)
   title = soup.title.text
   o = urlparse(url)
   base_url = o.netloc
   ext = tldextract.extract(url)
   domain_name = '.'.join(ext[1:])
   remove_stopword_word_tokens = remove_stopword(text)
   remove_stopword_text = ' '.join(remove_stopword_word_tokens)

   res = {
      'link' : url,
      'title' : title,
      'domain_name' : domain_name,
      'base_url' : base_url,
      'text' : text,
      'remove_stopword_word_tokens':remove_stopword_word_tokens,
      'remove_stopword_text': remove_stopword_text
   }

   with open(filename,'a') as f:
      json.dump(res,f)
      f.write('\n')

   return res

def remove_stopword(text):
   # nltk.download('stopwords')
   stop_words = set(stopwords.words('english')) 
   
   word_tokens = word_tokenize(text) 
   filtered_sentence = [w for w in word_tokens if not w in stop_words] 
   # print(filtered_sentence) 
   return filtered_sentence

# filename = 'test.json'
# url = 'https://sea.pcmag.com/smartphones/73/the-best-phones'
# input = get_page(url)
# res = save_page(input, filename, write_file=False)
# print(res)