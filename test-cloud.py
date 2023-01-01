import requests


invoke_url="https://x0ywfq3odb.execute-api.us-east-1.amazonaws.com/FirstTest1/predict"

data = {'url': 'https://raw.githubusercontent.com/AsMoh/Plant-Diseases-Classification/main/testing_images/TomatoEarlyBlight1.JPG'}

result = requests.post(invoke_url, json=data).json()
print(result)



