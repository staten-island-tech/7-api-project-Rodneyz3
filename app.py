import requests

def api():
    url = "https://aes.shenlu.me/api/v1/species"
    response=requests.get(url)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)

api()
    