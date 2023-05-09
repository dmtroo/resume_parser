import re


def find_salary(text):
    currencies = {
        r'\$': 'USD',
        '€': 'EUR',
        'UAH': 'UAH',
        'грн': 'UAH',
        '₴': 'UAH',
        'євро': 'EUR',
        'EUR': 'EUR',
        'EURO': 'EUR',
        'USD': 'USD',
        'є': 'EUR',
        'дол': 'USD',
        'грив': 'UAH'
    }

    salaries = []
    for cur, cur_standard in currencies.items():
        patterns = [
            fr"{cur}\s*(\d+((,\d{{3}})*|(\.\d+)?|(\s\d{{3}})*|\d*\.?\d*\s?[KMB]?))",
            fr"(\d+((,\d{{3}})*|(\.\d+)?|(\s\d{{3}})*|\d*\.?\d*\s?[KMB]?))\s*{cur}"
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, text)

            for match in matches:
                amount = match.group(1).replace(".", "").replace(",", ".").replace(" ", "")
                salaries.append((amount, cur_standard))

    return salaries
