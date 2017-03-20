from requests.auth import HTTPBasicAuth
import requests

url = 'http://httpbin.org/basic-auth/john/markovchain911'
auth = HTTPBasicAuth('john', 'markovchain911')

r = requests.get(url=url, auth=auth)
print r.status_code