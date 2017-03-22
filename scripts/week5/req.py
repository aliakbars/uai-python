import requests
import warnings
warnings.filterwarnings("ignore")

# Mencoba HTTP GET
params = {'q': 'Homer Simpson', 'format': 'json'}
r = requests.get('https://api.duckduckgo.com/', params=params)
# print
# print r.json()['Abstract']
# print

# Mencoba HTTP POST
payload = {'status': 'Kok belajar Python susah amat ya?'}
r = requests.post('http://httpbin.org/post', data=payload)
print r.json()
