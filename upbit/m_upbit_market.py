import requests
import pandas as pd


def upbitMarketCode(isDetail=False):
    if isDetail:
        querystring = {"isDetails": str(isDetail).lower()}
    else:
        querystring = {"isDetails": str(isDetail).lower()}

    url = "https://api.upbit.com/v1/market/all"

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


minute_unit_list = [1, 3, 5, 15, 10, 30, 60, 240]


def upbitMinuteCandle(market, unit, count, to=''):
    if (unit not in minute_unit_list):
        raise ValueError(
            "The unit isn't valid. Select in 1, 3, 5, 15, 10, 30, 60, 240.")

    url = "https://api.upbit.com/v1/candles/minutes/{}".format(str(unit))
    querystring = {"market": market, "count": str(count)}

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


def upbitDayCandle(market, count, to=''):
    url = "https://api.upbit.com/v1/candles/days"

    querystring = {"count": str(count), "market": market}

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


def upbitWeekCandle(market, count, to=''):
    url = "https://api.upbit.com/v1/candles/weeks"

    querystring = {"count": str(count), "market": market}

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


def upbitMonthCandle(market, count, to=''):
    url = "https://api.upbit.com/v1/candles/months"

    querystring = {"count": str(count), "market": market}

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


def upbitTick(market, count, to=''):
    url = "https://api.upbit.com/v1/trades/ticks"

    querystring = {"count": str(count), "market": market}

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


def upbitTicker(markets):
    url = "https://api.upbit.com/v1/ticker"

    querystring = {"markets": markets}

    try:
        response = requests.get(url, params=querystring)
        return pd.DataFrame(response.json())
    except Exception as e:
        raise e


def upbitOrderbook(markets):
    url = "https://api.upbit.com/v1/orderbook"

    querystring = {"markets": "KRW-BTC"}

    try:
        response = requests.get(url, params=querystring)

        res_json = response.json()
        orderbook_units = pd.DataFrame(res_json[0]['orderbook_units'])
        del res_json[0]['orderbook_units']

        return res_json, orderbook_units
    except Exception as e:
        raise e
