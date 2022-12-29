import requests

params = {
    "apiKey": "566314beaba2659752ff1dbd9dc20569",
    "modelName": "Address",
    "calledMethod": "searchSettlements",
    "methodProperties": {
        "CityName": "Лука-Мелешківська",
        "Limit": "50",
        "Page": "1"
    }
}


def find_address():
    r = requests.post("https://api.novaposhta.ua/v2.0/json/", json=params)
    print(f"Response: {r.json()}")
