import requests
import json

def get_countries():
    headers = {'Content-Type': 'application/json'}
    api_url = "https://restcountries.com/v2/all"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_country_code(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['alpha3Code']
    return None

def get_country_currency(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['currencies'][0]['code']
    return None

def transform(name: str, country_getter, 
              country_code_getter, country_currency_getter):
    countries = country_getter()
    code = country_code_getter(countries, name)
    currency = country_currency_getter(countries, name)

    return {"name": name, "country_code": code, "currency_code": currency}

def display_countries(country_getter):
    idx = 0
    countries = country_getter()

    for country in countries:
        print(idx, country['name'])
        idx += 1

    return countries

def show_country_info(country_displayer, country_getter, country_code_getter,
                      country_currency_getter, printer, get_input, transformer):
    countries = country_displayer(country_getter)
    
    selected_country_idx = int(get_input("Please choose a country: "))
    
    name = countries[selected_country_idx]['name']
    result = transformer(name, country_getter, country_code_getter,
                       country_currency_getter)
    printer(result)

# Start the app using the real implementations of each dependency
if __name__ == "__main__":
    show_country_info(display_countries, get_countries, get_country_code,
                      get_country_currency, print, input, transform)
