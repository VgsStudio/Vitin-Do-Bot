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


    #Lari
userID_lari = 'llaricasarini'

file_name_lari = 'last_seen_id_lari.txt'
frasestxt_lari = 'frases_lari.txt'


#Funções da lari-----------------------------------

def reply_to_tweets_lari(): # Responde a lari
    print('Procurando uns tweets da lari...', flush=True)
    while True:
        tempo_lari = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_lari)
        tempo_que_funciona = time.time() + tempo_lari #tempo de 5 minutos
        last_seen_id_lari = retrieve_last_seen_id(file_name_lari)
        
        print("Respondendo a lari...")
        while time.time() <= tempo_que_funciona:
            #Frases
            arquivoFrases = open(frasestxt_lari, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases
            time.sleep(6)
            mentions_lari = api.user_timeline(userID_lari, 
                            since_id = last_seen_id_lari,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_lari):
                last_seen_id_lari = mention.id
                store_last_seen_id(last_seen_id_lari, file_name_lari)
                if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                   api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

def store_tweets_lari(): # Armazena os Tweets do lari
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_lari = 5*60
        tempo_que_funciona =  time.time() + tempo_lari
        last_seen_id_lari = retrieve_last_seen_id(file_name_lari)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_lari = api.user_timeline(userID_lari, 
                           since_id = last_seen_id_lari,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_lari):
                print(str(mention.id) + ' - ' + mention.full_text,'- Lari')
                last_seen_id_lari = mention.id
                store_last_seen_id(last_seen_id_lari, file_name_lari)
    time.sleep(tempo_lari)


p_store_tweets_lari = threading.Thread(target=store_tweets_lari)
p_reply_to_tweets_lari = threading.Thread(target=reply_to_tweets_lari)