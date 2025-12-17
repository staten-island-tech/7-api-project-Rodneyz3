import requests
#project where user types animals common name to get scientific name
def api():
    url = "https://aes.shenlu.me/api/v1/species"
    response=requests.get(url)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    user=input("think of a common animal:")
    data = response.json()
    for i in data():
        if user in data[i]["common_name"] or user == data[i]["common_name"]:
            print(data[i]["scientific_name"])

api()
    