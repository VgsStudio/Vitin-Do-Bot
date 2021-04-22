import tweepy, time, random, threading

from os import environ

from func_global import *

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


    #luiza
userID_luiza = 'luizaskun'

file_name_luiza = 'luiza\\last_seen_id_luiza.txt'
frasestxt_luiza = 'frases_luiza.txt'


#Funções da luiza-----------------------------------

def reply_to_tweets_luiza(): # Responde a luiza
    print('Procurando uns tweets da luiza...', flush=True)
    while True:
        tempo_luiza = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_luiza)
        tempo_que_funciona = time.time() + tempo_luiza #tempo de 5 minutos
        last_seen_id_luiza = retrieve_last_seen_id(file_name_luiza)
        
        print("Respondendo a luiza...")
        while time.time() <= tempo_que_funciona:
            #Frases
            arquivoFrases = open(frasestxt_luiza, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases
            time.sleep(6)
            mentions_luiza = api.user_timeline(userID_luiza, 
                            since_id = last_seen_id_luiza,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_luiza):
                last_seen_id_luiza = mention.id
                store_last_seen_id(last_seen_id_luiza, file_name_luiza)
                if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                   api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

def store_tweets_luiza(): # Armazena os Tweets do luiza
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_luiza = 5*60
        tempo_que_funciona =  time.time() + tempo_luiza
        last_seen_id_luiza = retrieve_last_seen_id(file_name_luiza)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_luiza = api.user_timeline(userID_luiza, 
                           since_id = last_seen_id_luiza,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_luiza):
                print(str(mention.id) + ' - ' + mention.full_text,'- luiza')
                last_seen_id_luiza = mention.id
                store_last_seen_id(last_seen_id_luiza, file_name_luiza)
    time.sleep(tempo_luiza)


p_store_tweets_luiza = threading.Thread(target=store_tweets_luiza)
p_reply_to_tweets_luiza = threading.Thread(target=reply_to_tweets_luiza)