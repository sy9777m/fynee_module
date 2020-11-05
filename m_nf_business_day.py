import requests as rq
from bs4 import BeautifulSoup as bs


def business_day():
    url = 'https://finance.naver.com/sise/sise_index.nhn?code=KOSPI'

    res = rq.get(url)
    parse = bs(res.content)

    result = parse.find('span', {'id': 'time'}).text[0:10]
    result = result[0:4] + result[5:7] + result[8:10]

    return result