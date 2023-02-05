import requests
import json

token = '97133cd7b17ceafb2ab312bec048015d'

response = requests.post('https://pokemonbattle.me:5000/pokemons',headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "name": "Рокки",
    "photo": "https://avatanplus.com/files/resources/original/57ebd8c6b583d1577146c857.png"
})

print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons',headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Шах",
    "photo": ""
})

print(response_change.text)

response = requests.post('https://pokemonbattle.me:5000//trainers/add_pokeball',headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
   "pokemon_id": pokemon_id
})

print(response.text)
