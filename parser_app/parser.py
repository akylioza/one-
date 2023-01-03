import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "http://skyserial.video/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='th-item')
    serial_flm = []

    for item in items:
        serial_flm.append(
            {
                'title': item.find("a").get('href'),
                'title_text': item.find('a', class_='th-in fx-col th-hover').get_text(),
                'image': URL + item.find('a', class_='th-in fx-col th-hover').find('img').get('src')
            }
        )
    return serial_flm


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        serial_flm1 = []
        for page in range(0, 1):
            html = get_html(f'http://skyserial.video/serial/', params=page)
            serial_flm1.extend(get_data(html.text))
        return serial_flm1
    else:
        raise Exception('Error in parser func.....')