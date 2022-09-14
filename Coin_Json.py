# This python file is for video presentation and demonstrate Coin API ideas

import requests

coin_type = "BTC"
coin_type = "ETH"

function = "CURRENCY_EXCHANGE_RATE"

function = "DIGITAL_CURRENCY_MONTHLY"
function = "DIGITAL_CURRENCY_WEEKLY"
function = "DIGITAL_CURRENCY_DAILY"

# data type = csv or json

# API key ISTU2WJ8BK0TJ853

url = 'https://www.alphavantage.co/query?'\
      'function=DIGITAL_CURRENCY_MONTHLY' \
      '&symbol=BTC' \
      '&market=CAD' \
      '&apikey=ISTU2WJ8BK0TJ853'
r = requests.get(url)
data = r.json()

print(data)