import requests

response = requests.get(
    'https://oim.108122.xyz/words/random',
    headers={'X-Token': 'allyally'},  # your first name x2
)
print(response.json())

response = requests.get('https://oim.108122.xyz/mass')
data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

print(len(data))
print(data.keys())
print(type(data['data']))

towns = data['data']
print(type(towns))

# pprint(towns)
print(len(towns))

result = sorted(towns, key=lambda x: