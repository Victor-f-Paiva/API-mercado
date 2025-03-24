#até 25 requisições por dia
api_key = 'C4W3Y3FFTQ7ISXIQ'

import requests

ticker = 'PETR4.SAO'
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={ticker}&apikey={api_key}'
response = requests.get(url)
data = response.json()

for i in range(len(data)):
    print(data)
