import requests
import pytest

POKE_URL = "https://pokeapi.co/api/v2"
BOLA_URL = "https://swapi.info/api" # la otra api fea, la de star war, uuu


def get_dragon_pokemon_heights(limit=5):
    response = requests.get(f"{POKE_URL}/type/dragon")
    assert response.status_code == 200

    data = response.json()
    pokemons = data["pokemon"][:limit] # uuuu 

    heights = []

    for pp in pokemons:
        pokemon_url = pp["pokemon"]["url"]
        r = requests.get(pokemon_url, timeout=10)
        assert r.status_code == 200

        pokemon_data = r.json()
        heights.append(pokemon_data["height"])

    return heights


# ===========

def get_wookie_heights(limit=5):
    r = requests.get(f"{BOLA_URL}/species", timeout=10)
    assert r.status_code == 200

    species_list = r.json()

    wookie = next((s for s in species_list if s.get("name", "").lower() == "wookie"), None)
    assert wookie is not None, "No encontré la especie Wookie en /species"

    heights = []
    for person_url in wookie.get("people", []):
        rp = requests.get(person_url, timeout=10)
        assert rp.status_code == 200
        person = rp.json()

        h = person.get("height")
        if isinstance(h, str) and h.isdigit():
            heights.append(int(h))

        if len(heights) >= limit:
            break

    return heights


# ===========

def test_altura_promedio_dragon_vs_wookiee():
    dragon_heights = get_dragon_pokemon_heights(limit=5)
    wookie_heights = get_wookie_heights(limit=5)

    assert len(dragon_heights) > 0
    assert len(wookie_heights) > 0

    avg_dragon = sum(dragon_heights) / len(dragon_heights)
    avg_wookie = sum(wookie_heights) / len(wookie_heights)

    assert avg_wookie > avg_dragon

    print("/Dragon heights:", dragon_heights)
    print("/Wookie heights:", wookie_heights)
    print("/Avg dragon:", avg_dragon)
    print("/Avg wookie:", avg_wookie)
    






