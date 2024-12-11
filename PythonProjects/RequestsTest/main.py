import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'токен'
HEADER ={'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id" : "156817",
    "name" : "Чаризард",
    "photo_id" : 1
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.text)

pokemon_id = response_create.json()['id']


body_newname = {
    "pokemon_id" : pokemon_id,
    "name" : "Чаризард",
    "photo_id" : 1
}


response_newname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_newname) 
print(response_newname.text)

body_addpokeball = {
    "pokemon_id": pokemon_id
}

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball) 
print(response_addpokeball.text)