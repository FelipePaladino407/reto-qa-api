import pytest
import requests

URL = "https://pokeapi.co/api/v2"

@pytest.mark.parametrize("pokemon_name", [
    "pikachu",
    "charizard",
    "bulbasaur",
    "typhlosion",
    "gardevoir",
    "dragonite",
    "mewtwo"
    ])

def test_pokemon_debe_existir_retornar_200(pokemon_name):
    response = requests.get(f"{URL}/pokemon/{pokemon_name}", timeout=10)

    assert response.status_code == 200 

    data = response.json()
    # Vamo a ver si machea la respuesta:
    assert data["name"] == pokemon_name.lower()


def test_pokemon_noExiste_retorna_404():
    response = requests.get(f"{URL}/pokemon/SebaFeirres", timeout=10)

    assert response.status_code == 404
