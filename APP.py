################################################################################
# Application global read-only state using Singleton pattern
#
# Purpose: The App class is a singleton with the responsibility of managing
# the application's global read-only state.  This includes processing the
# application configuration file, and creating and providing access to the
# NOSQL database connection, News API, and Coins API.  See
# the Singleton pattern: https://en.wikipedia.org/wiki/Singleton_pattern.
#
# The app uses the News API to access news data and produce news reports:
# - https://github.com/mattlisiv/newsapi-python
# - https://newsapi.org/docs
# - https://www.alphavantage.co/documentation/
#
# The app uses the configparser module to read in a standard config file of
# key=value format: https://docs.python.org/3/library/configparser.html
#
# Author: Qin
# Contact: yangq90@mcmaster.ca
#
################################################################################
import requests
from newsapi.newsapi_client import NewsApiClient
import configparser
#   install boto3
import boto3
from botocore.config import Config

# App singleton contains all of the read-only state data that must be
# accessible across the application: configuration data, logging and the
# database connection.
class App():

    __instance = None

    # Setup the singleton based on the config file
    def setup(self):

        # Load the config file using the Config Parser module
        config = configparser.ConfigParser()
        config.read("config.cfg")

        # setup the News API module

        newsapi = NewsApiClient(api_key='1c5a24f2e65a4208be5bb56fc98e713a')

        # setup database connection based on the config file values
        my_config = Config(
            region_name='us-east-2',
            signature_version='v4',
            retries={
                'max_attempts': 10,
                'mode': 'standard'
            }
        )

        client = boto3.client('kinesis', config=my_config)

        s3 = boto3.resource('s3', region_name='us-east-2')
        dynamodb = boto3.client('dynamodb')

    # setup Coin API module
        # This is to setup communication with alphavantage and requesting BTC price
        url_BTC = 'https://www.alphavantage.co/query?' \
                  'function=DIGITAL_CURRENCY_DAILY' \
                  '&symbol=BTC' \
                  '&market=CAD' \
                  '&apikey=ISTU2WJ8BK0TJ853'
        r_BTC = requests.get(url_BTC)
        data_BTC = r_BTC.json()


        # This is to setup communication with alphavantage and requesting ETH price
        url_ETH = 'https://www.alphavantage.co/query?' \
                  'function=DIGITAL_CURRENCY_DAILY' \
                  '&symbol=ETH' \
                  '&market=CAD' \
                  '&apikey=ISTU2WJ8BK0TJ853'
        r_ETH = requests.get(url_ETH)
        data_ETH = r_ETH.json()


    # Creates or returns the singleton instance
    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = super(App, cls).__new__(cls)
            cls.__instance.setup()

        return cls.__instance
