from pathlib import Path
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract
import re
# import nltk
import codecs
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from url_normalize import url_normalize



def save_page(input_request, filename, write_file=True):
   html_doc = input_request['text']
   url = input_request['url']
   text_dict = clean_text(html_doc)
   text = text_dict['text']
   title = text_dict['title']
   domain_name = ''
   o = urlparse(url)
   base_url = o.netloc
   
   ext = tldextract.extract(url)
   domain_name = '.'.join(ext[1:])

   remove_stopword_word_tokens = remove_stopword(text)
   remove_stopword_text = ' '.join(remove_stopword_word_tokens)

   res = {
      'link' : url_normalize(url),
      'title' : title,
      'domain_name' : domain_name,
      'base_url' : base_url,
      'text' : text,
      'remove_stopword_word_tokens':remove_stopword_word_tokens,
      'remove_stopword_text': remove_stopword_text
   }

   with codecs.open(filename,'a',encoding='utf-8') as f:
      json.dump(res,f)
      f.write('\n')
   print('SAVE PAGE SUCCCESSFUL')

   return res

def remove_stopword(text):
   # nltk.download('stopwords')
   stop_words = set(stopwords.words('english')) 
   
   word_tokens = word_tokenize(text) 
   filtered_sentence = [w for w in word_tokens if not w in stop_words] 
   # print(filtered_sentence) 
   return filtered_sentence

def clean_text(raw_text):
   soup = BeautifulSoup(raw_text, 'html.parser')
   [s.extract() for s in soup('script')]
   [s.extract() for s in soup('style')]
   text = soup.text.strip().replace('\xa0', ' ').replace('\n',' ').replace('\t',' ').replace('\r',' ')
   text = re.sub(r"<!--(.|\s|\n)*?-->", "", text)
   title = ''
   try:
      title = soup.title.text
   except:
      pass
   return {
      'title': title,
      'text': text,
   }