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


    #thu
userID_thu = 'tutu_kosinski'

file_name_thu = 'thu\\last_seen_id_thu.txt'
frasestxt_thu = 'frases_thu.txt'


#Funções da thu-----------------------------------

def reply_to_tweets_thu(): # Responde a thu
    print('Procurando uns tweets da thu...', flush=True)
    while True:
        tempo_thu = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_thu)
        tempo_que_funciona = time.time() + tempo_thu #tempo de 5 minutos
        last_seen_id_thu = retrieve_last_seen_id(file_name_thu)
        
        print("Respondendo a thu...")
        while time.time() <= tempo_que_funciona:
            #Frases
            arquivoFrases = open(frasestxt_thu, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases
            time.sleep(6)
            mentions_thu = api.user_timeline(userID_thu, 
                            since_id = last_seen_id_thu,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_thu):
                last_seen_id_thu = mention.id
                store_last_seen_id(last_seen_id_thu, file_name_thu)
                if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                   api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

def store_tweets_thu(): # Armazena os Tweets do thu
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_thu = 5*60
        tempo_que_funciona =  time.time() + tempo_thu
        last_seen_id_thu = retrieve_last_seen_id(file_name_thu)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_thu = api.user_timeline(userID_thu, 
                           since_id = last_seen_id_thu,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_thu):
                print(str(mention.id) + ' - ' + mention.full_text,'- thu')
                last_seen_id_thu = mention.id
                store_last_seen_id(last_seen_id_thu, file_name_thu)
    time.sleep(tempo_thu)


p_store_tweets_thu = threading.Thread(target=store_tweets_thu)
p_reply_to_tweets_thu = threading.Thread(target=reply_to_tweets_thu)