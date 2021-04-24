import tweepy, time, random, threading

from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def tweet_trap():
    while True:
        time.sleep(30*60) #30 segundos * 60 -> 30 minutos.
        
        vitin_tweets =  'vitin_tweets.txt' #Arquivo das Frases

        try:
            #Frases
            arquivoFrases = open(vitin_tweets, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases

            api.update_status('%s' % frase) # Tweetar frase
            print('%s -> Tweet' % frase) # Frase postada
        except tweepy.TweepError as error:
            if error.api_code == 187:
                print('Status duplicado')

p_tweet_trap = threading.Thread(target = tweet_trap )
