import requests
from pprint import pprint
from dotenv import load_dotenv
import os


#response = requests.get('https://oim.108122.xyz/words/random')
#print(response.json())   # a random word!

#response = requests.get('https://oim.108122.xyz/mass')
#data = response.json()

#print(data['name'])       # 'Massachusetts'
#print(data['governor'])   # 'Maura Healey'

#for town in data['data'][:5]:
#    print(f"{town['name']}: pop {town['population']:,}")

#response = requests.get(
#   'https://oim.108122.xyz/words/random',
#   headers={'X-Token': 'alicealice'},  # your first name x2)
#print(response.json())

# GET: read all messages
# requests  = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#    print(msg)

# POST: send a message (1-140 characters)
# requests.post('https://oim.108122.xyz/message',
#              json={'message': 'Hello from Ally!'},
#              headers={'X-Token': 'allyally'})

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')
url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')

print(url)
data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")

