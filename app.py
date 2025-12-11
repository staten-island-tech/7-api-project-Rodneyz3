import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Arceus")
print(pokemon)


import requests

def spoon(reciple):
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query=pizza&apiKey=17b0dfdac1e6454d9f3bc9e4cb27b568{reciple.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    return {
        "id": data["id"]
    }

food = spoon("Pesto Veggie Pizza.")
print(food)
    
