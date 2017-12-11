import requests
from requests_oauthlib import OAuth1

payload = {'q': 'news'}
url = 'https://api.twitter.com/1.1/search/tweets.json'

auth = OAuth1(
    'AGsVhqXmwc9fGM82xVcIpRUcj',
    'nN3HKcMOLlyy91RjOaFyoFe64GwRpSBObaC68fkJEVDHyjntfw',
    '826265268867432449-KLaZ2b8afiGmuINEPKmqA4DjWv4ENQT',
    'W3nJGED61ALQOerEC6Esl2A74hHeDI4Z8fRSqG9D1besv'
)

r = requests.get(url, params=payload, auth=auth)

print(r.content)
