import requests as rq
import pandas as pd
import json
import io
from datetime import date
from bs4 import BeautifulSoup as bs


class KrxDelisting:
    def __init__(self):
        self.load()

    def load(self):
        otp_url = 'https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_dellist_isu&name=form&_=1604145804003'
        otp_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
        }
        res = rq.get(otp_url, headers=otp_header)
        otp = res.text

        url = 'https://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx'
        url_data = {
            'mktsel': 'ALL',
            'pagePath': '/contents/COM/FinderDelListIsu.jsp',
            'code': otp
        }
        url_headers = {
            'referer': 'https://marketdata.krx.co.kr/mdi',
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
        }

        result = rq.post(url, data=url_data, headers=url_headers)

        krx_delisting = pd.DataFrame(json.loads(result.text)['result'])

        return krx_delisting


class KrxListing:

    def __init__(self, business_day):
        self.business_day = business_day

    def krx_stock_listing(self):
        otp_url = 'https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp' \
                  + '&market_gubun=' + 'ALL' \
                  + '&sect_tp_cd=' + 'ALL' \
                  + '&isu_cdnm=' + '전체' \
                  + '&secugrp=' + 'ST' \
                  + '&stock_gubun=' + 'on' \
                  + '&schdate=' + self.business_day

        otp_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/mdi',
        }

        res = rq.get(otp_url, headers=otp_header)
        otp = res.text

        url = 'https://file.krx.co.kr/download.jspx'
        url_data = {
            'code': otp
        }
        url_header = {
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/'
        }

        result = rq.post(url, data=url_data, headers=url_header)

        krx_listing = pd.read_csv(io.BytesIO(result.content))

        return krx_listing

    def krx_etf_listing(self):
        otp_url = 'https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp' \
                  + '&market_gubun=' + 'ALL' \
                  + '&sect_tp_cd=' + 'ALL' \
                  + '&isu_cdnm=' + '전체' \
                  + '&secugrp=' + 'EF' \
                  + '&stock_gubun=' + 'on' \
                  + '&schdate=' + self.business_day

        otp_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/mdi',
        }

        res = rq.get(otp_url, headers=otp_header)
        otp = res.text

        url = 'https://file.krx.co.kr/download.jspx'
        url_data = {
            'code': otp
        }
        url_header = {
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/'
        }

        result = rq.post(url, data=url_data, headers=url_header)

        etf_listing = pd.read_csv(io.BytesIO(result.content))

        return etf_listing

    def krx_elw_listing(self):
        otp_url = 'https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp' \
                  + '&market_gubun=' + 'ALL' \
                  + '&sect_tp_cd=' + 'ALL' \
                  + '&isu_cdnm=' + '전체' \
                  + '&secugrp=' + 'EW' \
                  + '&stock_gubun=' + 'on' \
                  + '&schdate=' + self.business_day

        otp_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/mdi',
        }

        res = rq.get(otp_url, headers=otp_header)
        otp = res.text

        url = 'https://file.krx.co.kr/download.jspx'
        url_data = {
            'code': otp
        }
        url_header = {
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/'
        }

        result = rq.post(url, data=url_data, headers=url_header)

        elw_listing = pd.read_csv(io.BytesIO(result.content))

        return elw_listing

    def krx_etn_listing(self):
        otp_url = 'https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp' \
                  + '&market_gubun=' + 'ALL' \
                  + '&sect_tp_cd=' + 'ALL' \
                  + '&isu_cdnm=' + '전체' \
                  + '&secugrp=' + 'EN' \
                  + '&stock_gubun=' + 'on' \
                  + '&schdate=' + self.business_day

        otp_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/mdi',
        }

        res = rq.get(otp_url, headers=otp_header)
        otp = res.text

        url = 'https://file.krx.co.kr/download.jspx'
        url_data = {
            'code': otp
        }
        url_header = {
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/'
        }

        result = rq.post(url, data=url_data, headers=url_header)

        etn_listing = pd.read_csv(io.BytesIO(result.content))

        return etn_listing

    def krx_ect_listing(self):
        otp_url = 'https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp' \
                  + '&market_gubun=' + 'ALL' \
                  + '&sect_tp_cd=' + 'ALL' \
                  + '&isu_cdnm=' + '전체' \
                  + '&secugrp=' + 'Y' \
                  + '&stock_gubun=' + 'on' \
                  + '&schdate=' + self.business_day

        otp_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/mdi',
        }

        res = rq.get(otp_url, headers=otp_header)
        otp = res.text

        url = 'https://file.krx.co.kr/download.jspx'
        url_data = {
            'code': otp
        }
        url_header = {
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
            'referer': 'https://marketdata.krx.co.kr/'
        }

        result = rq.post(url, data=url_data, headers=url_header)

        ect_listing = pd.read_csv(io.BytesIO(result.content))

        return ect_listing

    # from 1990.01.03
    def naver_finance_day_price(self, symbol):
        first_day = date(1990, 1, 3)
        today = date.today()

        request_days = (today - first_day).days

        url = 'https://fchart.stock.naver.com/sise.nhn?symbol=' + symbol + '&timeframe=day&count=' + str(request_days) + '&requestType=0'
        url_header = {
            'User-Agent': 'Chrome/86.0.4240.111 Safari/537.36',
        }

        res = rq.get(url, headers=url_header)
        parse = bs(res.content)

        items = parse.find_all('item')

        price_df_columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        day_price_df = pd.DataFrame(None, columns=price_df_columns)

        for i in items:
            data = i.attrs['data'].split('|')
            temp_dict = {}
            for index, data in enumerate(data):
                temp_dict[price_df_columns[index]] = data
            day_price_df = day_price_df.append(temp_dict, ignore_index=True)

        return day_price_df
