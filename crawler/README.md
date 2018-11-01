# crawler for Samsung mobile phone

- add seed url list in seed.txt ex.

```python
http://xxx.xxx.com
http://yyyy.com
```

- usage

```bash
python crawler.py
```

- output
   - visited_q.txt --> store visited queue
   - frontier_q.txt --> store frontier queue
   - lists_html.txt --> store crawled webpage url
   - test.json (You can config this filename in crawler.py)
      - store json of page

```json
{
   "link": "url of the webpage",
   "title": "title of the webpage", 
   "domain_name": "domain name of url ex. pcmag.com", 
   "base_url": "base url of url ex. sea.pcmag.com", 
   "text": "text from webpage (already extracted by BeautifulSoup)",
   "remove_stopword_word_tokens": "listword already removed stopword (using nltk)",
   "remove_stopword_text":  "using spacebar join remove_stopword_word_tokens"
   }

```