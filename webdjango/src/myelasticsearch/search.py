from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import requests
import json
from myelasticsearch.summarizer import summarizer

class searcher():
      localhost = 'http://localhost:9200/'
      search_url = '_search?q='

      def __init__(self):
            pass

      def search(self,query, sum_op = 'url',SENTENCES_COUNT=2):
            url = self.localhost + self.search_url + query
            r = requests.get(url, params={'size':50})
            res_raw = json.loads(r.text)
            search_result = []
            rank = 1
            print("test",  len(res_raw['hits']['hits']))
            for one_res in res_raw['hits']['hits']:
                  one_res_source = one_res['_source']
                  one_res_source['score'] = one_res['_score']
                  del one_res_source['remove_stopword_text']
                  
                  if sum_op != 'no':
                        one_res_source['summary'] = summarizer(one_res_source, SENTENCES_COUNT, op = sum_op)
                  one_res_source['rank'] = rank
                  rank = rank + 1
                  search_result.append(one_res_source)
            return search_result

# if __name__ == "__main__":
#       obj = searcher()
#       q = 'note9'
#       print(obj.search(q,sum_op='text'))