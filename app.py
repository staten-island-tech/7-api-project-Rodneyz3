
import requests

def api():
    url = "https://aes.shenlu.me/api/v1/species"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data!")
        return
    
    

    
    data = response.json()

    for animal in data:
        print(animal["common_name"])
    found = False

    user = input("Write a common name from the list:").lower()

   

    for species in data: 
        common_name = species.get("common_name", "").lower()

        if user == common_name:
            print("Scientific name:", species.get("scientific_name"))
            found = True
            break

    if not found:
        print("Animal not found.")

api()