import tweepy
import time

consumer_key = 'E8unZOskXX4fRJkEt7HizREwS'
consumer_secret = 'QD0bwerax4gJp2F7GVbukBzqrGDueDTb9WhhezBJQz0TjH7lRI'
access_token = '1369432777742049285-XLgRqC0F3aGsHH8veSLI4qxNAVemLt'
access_token_secret = 'vC9ddfcbKj4XLfHDvRddlVPy7hrVKJeyaQAbXDVR3ZxDo'

print('Bot da perfeição', flush=True)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = 'llaricasarini'

mentions = api.user_timeline(userID, 
                           tweet_mode = 'extended'
                           )

# MENÇÕES
for info in mentions[:100]:
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")