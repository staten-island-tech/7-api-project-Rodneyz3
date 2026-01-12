import tkinter as tk
import requests


def api():
    url = "https://aes.shenlu.me/api/v1/species"
    data = requests.get(url).json()


    for animal in data:
        print(animal["common_name"])


    user_choice = name_entry.get().lower()
   
    for species in data:
        if user_choice == species.get("common_name", "").lower():
            fact_label.config(text=f"Scientific: {species.get('scientific_name')}")
            return


    fact_label.config(text="Not found")




root = tk.Tk()
root.title("Converter")


tk.Label(root, text="Type name from terminal:").pack(pady=5)


name_entry = tk.Entry(root)
name_entry.pack(pady=5)


btn = tk.Button(root, text="Convert & Print List", command=api)
btn.pack(pady=10)


fact_label = tk.Label(root, text="")
fact_label.pack(pady=10)


root.mainloop()

