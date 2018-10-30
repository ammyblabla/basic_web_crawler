from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import requests

ua = UserAgent() # From here we generate a random user agent

# Main function
class proxy ():
   def __init__(self):
      self.page_number = 0
      self.proxies = self.get_proxies()
      self.proxy = None
      self.header = None

   def get_proxies(self):
      proxies = []
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
      req = None
      try:
         if self.page_number % 5 == 0:
            proxy_index_http = self.random_proxy()
            proxy_index_https = self.random_proxy()
            proxy_http = self.proxies[proxy_index_http]
            proxy_https = self.proxies[proxy_index_https]
         # while(proxy_https['Https'] != 'Yes'):
         #    proxy_https = self.proxies[proxy_index_https]
         self.proxy = {
            'http' : f"""http://{proxy_http['ip']}:{proxy_http['port']}""",
            'https' : f"""http://{proxy_https['ip']}:{proxy_https['port']}"""
         }
         self.headers = self.get_header()
         req = requests.get(url, timeout=2, proxies=self.proxy, headers=self.headers, verify=True)
      except Exception as e:
         print(e)
         print('GET PAGE ERROR!')
      return req

   def random_proxy(self):
      return random.randint(0, len(self.proxies) - 1)

   def get_header(self):
      # Please change your email
      return {
        'User-Agent': ua.random,
        'from': 'natnaree.as@ku.th'
      }
      

# if __name__ == '__main__':
#    proxy_obj = proxy()
#    r = proxy_obj.request_page('https://sea.pcmag.com/')
#    print(r.status_code)
