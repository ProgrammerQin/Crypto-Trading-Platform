# This Python File is to demonstrate how to implement NewsAPI

#   1c5a24f2e65a4208be5bb56fc98e713a
#   https://newsapi.org/v2/everything?q=tesla&from=2022-06-02&sortBy=publishedAt&apiKey=1c5a24f2e65a4208be5bb56fc98e713a

# $ pip install newsapi-python
# Init

from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='1c5a24f2e65a4208be5bb56fc98e713a')


top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')

all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2022-06-30',
                                      to='2022-07-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

url = ('https://newsapi.org/v2/everything?'
       'q=Bitcoin&'
       'from=2022-07-23&'
       'sortBy=popularity&'
       'apiKey=1c5a24f2e65a4208be5bb56fc98e713a')

response = requests.get(url)
sources = newsapi.get_sources()

print(response.json())
print(top_headlines)
print(sources)
print(all_articles)