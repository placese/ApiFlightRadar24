import requests
import json
from datetime import datetime as dt

URL_BASE = f'https://api.flightradar24.com/common/v1/flight/list.json?&fetchBy=flight&page=1&limit=25&query='
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
           'accept': '*/*'}


def api_get():
    URL = set_url()
    response = requests.get(URL, headers=HEADERS)
    text = response.text
    dict_text = dict(json.loads(text))
    li = list(dict_text.get('result').get('response').get('data'))
    info = li[set_date(li)]
    origin_lat = float(info['airport']['origin']['position']['latitude'])
    origin_long = float(info['airport']['origin']['position']['longitude'])
    destination_lat = float(info['airport']['destination']['position']['latitude'])
    destination_long = float(info['airport']['destination']['position']['longitude'])
    origin = [origin_lat, origin_long]
    destination = [destination_lat, destination_long]
    return [origin, destination]


def set_date(li):
    print("Выберите время отправления: ")
    for counter, i in enumerate(li):
        # if dt.fromtimestamp(i.get('time').get('real').get('departure')) is NoneType:
        #     continue
        print(f"{counter}:", dt.fromtimestamp(int(i.get('time').get('real').get('departure'))))

        print('---------------------------')
    n = int(input())
    return n


def set_url():
    print("Введите номер рейса: ")
    URL = URL_BASE + input()
    print(URL)
    return URL


if __name__ == '__main__':
    api_get()
