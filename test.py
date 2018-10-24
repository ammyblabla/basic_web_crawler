import requests
url = 'http://bit.ly/2PdcLZR'
r = requests.get(url, timeout = 2,allow_redirects=False)
print(r.status_code)
print(r.headers)
print(r.text)