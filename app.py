import tkinter as tk
tk.geometry(400,200)



import requests

def api():
    url = "https://aes.shenlu.me/api/v1/species"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data!")
        return

    user = input("Write a common name ").lower()
    data = response.json()

    found = False

    for species in data: 
        common_name = species.get("common_name", "").lower()

        if user == common_name:
            print("Scientific name:", species.get("scientific_name"))
            found = True
            break

    if not found:
        print("Animal not found.")

api()