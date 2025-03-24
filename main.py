import requests
from meu_token_brapi import token

#até 15 mil requisições por mês
ticker = 'PETR4'
url = f"https://brapi.dev/api/quote/{ticker}?token={token}"
params1 = {
    'interval': '5d',
}
params2 = {
    'interval': '1wk'
}
params3 = {
    'interval': '1mo'
}
 
response = requests.get(url, params=params1)
 
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
