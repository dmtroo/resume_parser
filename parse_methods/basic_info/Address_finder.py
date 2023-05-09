import requests

params = {
    "apiKey": "566314beaba2659752ff1dbd9dc20569",
    "modelName": "Address",
    "calledMethod": "searchSettlements",
    "methodProperties": {
        "CityName": "",
        "Limit": "1",
        "Page": "1"
    }
}


def find_address(parsed_json):
    for sentence in parsed_json:
        for token in sentence['tokens']:
            if token['upos'] == 'PROPN':
                params['methodProperties']['CityName'] = token['form']
                address = check_address(params, token['form'])
                if address:
                    return address


def check_address(parameters, city):
    r = requests.post("https://api.novaposhta.ua/v2.0/json/", json=parameters)
    res = r.json()
    if res['success'] and res['data'][0]['TotalCount'] > 0 and \
            res['data'][0]['Addresses'][0]['Present'].split()[1].rstrip(',') == city:
        return res['data'][0]['Addresses'][0]['Present']
