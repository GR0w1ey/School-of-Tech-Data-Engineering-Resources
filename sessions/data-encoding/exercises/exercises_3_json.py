import json

with open('hitchhikers_guide_characters.json', 'w') as character_data:
    characters = {
        'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
        }
    }

    json.dump(characters, character_data)
