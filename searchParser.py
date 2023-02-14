import requests
from bs4 import BeautifulSoup


def find_on_azlyrics(text):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    first_req = requests.get('https://www.azlyrics.com/geo.js', headers=headers)

    x = first_req.text.split('\n')[7][30:-3]

    print(x)
    print(f'searching for: {text}')
    req = requests.get('https://search.azlyrics.com/search.php', {'q': text, 'x': x}, headers=headers)
    print(req.url)
    bs = BeautifulSoup(req.text, 'lxml')

    hrefs = []

    for i in bs.findChildren('td', {'class': 'visitedlyr'}):
        a = i.findChild('a')["href"]
        hrefs.append(a)

    if len(hrefs) == 0:
        return req.url, None

    req2 = requests.get(hrefs[0])
    bs2 = BeautifulSoup(req2.text, 'lxml')

    div = max(list(bs2.findChild('div', {'class': 'col-lg-8'}).children), key=lambda i: len(i))

    return req2.url, div.text

