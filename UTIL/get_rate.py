import tweepy
import time
from os import environ


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

print('Get Rate', flush=True)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


data = api.rate_limit_status()
while True:
    print (data['resources']['statuses']['/statuses/user_timeline'])
    print(data['resources']['statuses']['/statuses/mentions_timeline'])
    time.sleep(5)