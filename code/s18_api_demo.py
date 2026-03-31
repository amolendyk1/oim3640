import requests

response = requests.get('https://oim.108122.xyz/words/random')
print(response.json())   # a random word!

response = requests.get('https://oim.108122.xyz/mass')
data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

print(len(data))
print(data.keys())
print(type(data['data']))


