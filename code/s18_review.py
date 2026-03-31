words = 'the cat sat on the mat'.split()
print(len(words))
print(len(set(words)))
print(set(words))

def mystery(s):
    return len(set(s)) == len(s)

print(mystery('hello'))
print(mystery('world'))

freq = {'a': 3, 'b': 1, 'c': 2}
result = sorted(freq.items(), key=lambda x: x[1])
print(result)

try:
    age = int(input('Your age: '))
    print(f'You are {age} years old')
except ValueError:
    print('That is not a valid number!')

scores = {'Alice': 95, 'Bob': 87}

try:
    name = input('Student name: ')
    print(f'{name}: {scores[name]}')
except KeyError:
    print(f'{name} not found')

import requests

response = requests.get('https://oim.108122.xyz/words/random')
print(response.json())   # a random word!