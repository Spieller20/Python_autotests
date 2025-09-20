import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '{{YOUR_POKEMONBATTLE_TOKEN}}'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER = '38081'
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER})
    assert response.status_code == 200

def test_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER})

    assert response_get.json()['data'][0]['id'] == '38081'
