import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '{{YOUR_POKEMONBATTLE_TOKEN}}'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
create_pokemmon = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post (url = f'{URL}/pokemons', headers = HEADER,  json = create_pokemmon)
print(response_create.text)

pokemon_id = response_create.json()['id']

new_name_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}

response_new_name_pokemon = requests.put (url = f'{URL}/pokemons', headers = HEADER,  json = new_name_pokemon)
print(response_new_name_pokemon.text)

add_pokeball = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER,  json = add_pokeball)

print(response_add_pokeball.text)
