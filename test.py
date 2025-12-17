import requests

def api():
    url = "https://aes.shenlu.me/api/v1/species"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data!")
        return

    user = input("Think of a common animal: ").lower()
    data = response.json()

    for species in data:
        if user in species["common_name"].lower():
            print("Scientific name:", species["scientific_name"])
            return

    print("Animal not found.")

api()