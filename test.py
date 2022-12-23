import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://raw.githubusercontent.com/AsMoh/Plant-Diseases-Classification/main/Cornheal.jpg'}

result = requests.post(url, json=data).json()
print(result)



