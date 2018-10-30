from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import requests

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

# Main function
class proxy ():
   def __init__(self):
      self.page_number = 0
      self.proxies = self.get_proxies()
      self.headers = {
         'User-Agent': 'Natnaree Asavaseri User Agent 1.0',
         'From': 'natnaree.as@ku.th'
      }

   def get_proxies(self):
      print('eieieie')
      proxies_req = Request('https://www.sslproxies.org/')
      proxies_req.add_header('User-Agent', ua.random)
      proxies_doc = urlopen(proxies_req).read().decode('utf8')

      soup = BeautifulSoup(proxies_doc, 'html.parser')
      proxies_table = soup.find(id='proxylisttable')

      # Save proxies in the array
      for row in proxies_table.tbody.find_all('tr'):
         proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
         })
      return proxies

   def request_page(self,url):
      if self.page_number % 10 == 0:
         proxy_index = self.random_proxy()
         # req.set_proxy(self.proxy['ip'] + ':' + self.proxy['port'], 'http')
         self.proxy = {
            'http' : f"""http://{proxies[proxy_index]['ip']}:{proxies[proxy_index]['port']}"""
         }
      req = requests.get(url, timeout=2, proxies=self.proxy)
      print(self.proxy)
      return req
   # Choose a random proxy

   def random_proxy(self):
      return random.randint(0, len(self.proxies) - 1)

if __name__ == '__main__':
   proxy_obj = proxy()
   r = proxy_obj.request_page('https://sea.pcmag.com/')
   print(r.status_code)
