import requests
from pprint import pprint


URL = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
CURRENCIES = ["USD", "EUR", "GBP", "RUB", "CNY", 'KRW', 
              "TRY", "AZN", "KZT", "TJS", "TJS", "AED"]
FLAGS = {
    'USD': '🇺🇸', 'EUR': '🇪🇺','GBP': '🇩🇪', 'RUB': '🇷🇺',
    'CNY': '🇨🇳', 'KRW': '🇰🇷', 'TRY': '🇹🇷', 'AZN': '🇹🇲', 
    'KZT': '🇰🇿', 'TJS': '🇹🇯', 'TJS': '🇰🇬', 'AED': '🇦🇪'
}

def get_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        return False


def filter_contries():
    content = get_data()
    if content:
        data = []
        for country in content:
            if country['Ccy'] in CURRENCIES:
                data.append(country)
        return data

    return False


def make_text(data):
    sana = data[0]['Date']
    text = f'🇺🇿<a href="https://t.me/back1145bot">Markaziy bank sanasi {sana}</a>\n'
    plain_text = "1 {} {} = {}\n"
    for country in data:
        text += plain_text.format(
            FLAGS[country['Ccy']], 
            country['CcyNm_UZ'],
            country['Rate']
        )

    text += "@valyutalar_bot - Valyuta Kalkulyatori"

    return text


def to_uzs(amount, data):
    text = ''
    plain_text = "{} {} {} = {}\n"
    for country in data:
        price = amount * float(country['Rate'])
        price = f'{price:.2f}'
        formatted_text = plain_text.format(
            amount, FLAGS[country['Ccy']],
            country['CcyNm_UZ'], price
        )
        text += formatted_text
    return text


def from_uzs(amount, data):
    text = ''
    plain_text = "{} 🇺🇿 UZS = {} {}\n"
    for country in data:
        price = amount / float(country['Rate'])
        price = f'{price:.2f}'
        formatted_text = plain_text.format(
            amount, FLAGS[country['Ccy']],
            price
        )
        text += formatted_text
    return text


def get_calculated_text(amount, data):
    text1 = to_uzs(amount, data)
    text2 = from_uzs(amount, data)
    return text1 + '\n' + text2

# data = filter_contries()
# text = make_text(data)
# print(text)
# final_text = get_calculated_text(100, data)
# print(final_text)