import tweepy
import time
from os import environ


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


print('Bot da perfeição', flush=True)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = 'anthony_vigario' # Usuário

mentions = api.user_timeline(userID, 
                           tweet_mode = 'extended'
                           )

# MENÇÕES
for info in reversed(mentions[:100]):
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")