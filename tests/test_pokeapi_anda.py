import requests

URL = "http://pokeapi.co/api/v2"

def test_pokemon_typhlosion_exists():
    response = requests.get(f"{URL}/pokemon/typhlosion", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "typhlosion"
