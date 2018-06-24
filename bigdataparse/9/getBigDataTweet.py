#!usr/bin/env/python
# -*- coding: utf-8 -*-
#coding UTF-8

from requests_oauthlib import OAuth1Session
import json 

CONSUMER_KEY = "2WdR3K10xf7AMd72yeLvRtZH8"
CONSUMER_SECRET = "WBwmFM2LI1sTMA1c9WTFgHp1Y1AQsPt2m5VsBgs4r91lMlfViS"
ACCESS_TOKEN = "1009105919236440066-xxUM83DfTD2kRoOhH0xqdbNuaPJdmh"
ACCESS_SECRET = "Be9afq6LYgvZCGn0QBOUaFGvAWrvfgXHnqS0k994wLPNw"
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#api = tweepy.API(auth)
twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
url = "http://api.twitter.com/1.1/search/tweets.json"
params = {'q': "サッカー", 'count': 10, 'lang':"ja"}
req = twitter.get(url, params=params)
if req.status_code == 200:
    tweets = json.loads(req.text)
    for tweet in tweets['statuses']:
        print(tweet['text'].replace('\n', ' '))
else:
    print ("ERROR: %d" %req.status_code)