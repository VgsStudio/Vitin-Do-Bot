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

    #thony
userID_thony = 'sanickBR'

file_name_thony = 'thony/last_seen_id_thony.txt'
frasestxt_thony = 'thony/frases_thony.txt'

#Funções do Thony-----------------------------------

 
def reply_to_tweets_thony(): # Responde o thony
    print('Procurando uns tweets do thony...', flush=True)
    while True:
        tempo_thony = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_thony)
        tempo_que_funciona = time.time() + tempo_thony #tempo de 5 minutos
        last_seen_id_thony = retrieve_last_seen_id(file_name_thony)
        
        print("Respondendo o thony...")
        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_thony = api.user_timeline(userID_thony, 
                            since_id = last_seen_id_thony,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_thony):
                last_seen_id_thony = retrieve_last_seen_id(file_name_thony)
                if last_seen_id_thony < mention.id:
                    last_seen_id_thony = mention.id
                    store_last_seen_id(last_seen_id_thony, file_name_thony)

                    #Frases
                    arquivoFrases = open(frasestxt_thony, 'r')
                    arrayFrases = arquivoFrases.read().split('\n')
                    frase = random.choice(arrayFrases)
                    #Frases

                    if ('RT @' not in mention.full_text): #Evita responder RTs sem comentários                 
                        api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)
                        try:
                            api.create_favorite(mention.id)
                            api.retweet(mention.id)   
                        except tweepy.TweepError as error:
                                if error.api_code == 139:
                                    print('Tweet já favoritado...')  

                else:
                    break

                print("Parando de responder.")
            
        

def store_tweets_thony(): # Armazena os Tweets do thony
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_thony = 5*60
        tempo_que_funciona =  time.time() + tempo_thony
        last_seen_id_thony = retrieve_last_seen_id(file_name_thony)


        while time.time()<=tempo_que_funciona:
            time.sleep(6)
            mentions_thony = api.user_timeline(userID_thony, 
                           since_id = last_seen_id_thony,
                           include_rt = False,
                           tweet_mode = 'extended') 
            for mention in reversed(mentions_thony):
                print(str(mention.id) + ' - ' + mention.full_text, '- thony')
                last_seen_id_thony = retrieve_last_seen_id(file_name_thony)
                if last_seen_id_thony < mention.id:
                    last_seen_id_thony = mention.id
                    store_last_seen_id(last_seen_id_thony, file_name_thony)
                    if 'RT @' not in mention.full_text: #Evita curtir RTs sem comentários
                        try:
                            api.create_favorite(mention.id)
                            api.retweet(mention.id)
                        except tweepy.TweepError as error:
                                    if error.api_code == 139:
                                        print('Tweet já favoritado...')  
                else:
                    break


    print("Parando de armazenar...")
    time.sleep(tempo_thony)

p_store_tweets_thony = threading.Thread(target=store_tweets_thony)
p_reply_to_tweets_thony = threading.Thread(target=reply_to_tweets_thony)
