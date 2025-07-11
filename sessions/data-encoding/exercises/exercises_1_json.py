import json

with open('menu_items.json', 'r') as menu_data:
    menu_items = json.load(menu_data)
    items = menu_items["menu"]["items"]
    for item in menu_items["menu"]["items"]:
        print(item["id"])
