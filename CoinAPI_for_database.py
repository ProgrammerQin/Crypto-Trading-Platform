#   This python file is to test and demonstrate coinAPI for Database Use

#   Alpha vantage API key free:  AEGJDU540F597MXQ

#   git clone https://github.com/RomelTorres/alpha_vantage.git
#   pip install -e alpha_vantage
#   python -m pip install SomePackage
#   pip3 install alpha_vantage
#   pip3 install gitpython

import requests
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

def get_BTC_price_json(self):

    url_BTC = 'https://www.alphavantage.co/query?' \
              'function=DIGITAL_CURRENCY_DAILY' \
              '&symbol=BTC' \
              '&market=CAD' \
              '&apikey=ISTU2WJ8BK0TJ853'

    r_BTC = requests.get(url_BTC)

    data_BTC = r_BTC.json()

    return data_BTC


def get_ETH_price_json(self):

    url_ETH = 'https://www.alphavantage.co/query?' \
              'function=DIGITAL_CURRENCY_DAILY' \
              '&symbol=ETH' \
              '&market=CAD' \
              '&apikey=ISTU2WJ8BK0TJ853'

    r_ETH = requests.get(url_ETH)

    data_ETH = r_ETH.json()

    return data_ETH

