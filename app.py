import requests

def api(reciple):
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query=pizza&apiKey=17b0dfdac1e6454d9f3bc9e4cb27b568{reciple.lower()}")
