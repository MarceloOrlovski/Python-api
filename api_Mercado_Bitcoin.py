import requests

url= 'https://www.mercadobitcoin.net/api/BTC/ticker/'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print(response_dict.keys()) 

print("Total repositorios:", response_dict['ticker'])

repo_dicts = response_dict['ticker']

print("Repositorios Return:", len(repo_dicts))