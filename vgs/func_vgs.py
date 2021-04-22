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

    #Vitin
userID_vgs = 'vgs_studio'

file_name_vgs = 'vgs\\last_seen_id_vgs.txt'
frasestxt_vgs = 'frases_vitin.txt'

#Funções do Vitin-----------------------------------

 
def reply_to_tweets_vgs(): # Responde o Vgs
    print('Procurando uns tweets do Vgs...', flush=True)
    while True:
        tempo_vgs = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_vgs)
        tempo_que_funciona = time.time() + tempo_vgs #tempo de 5 minutos
        last_seen_id_vgs = retrieve_last_seen_id(file_name_vgs)
        
        print("Respondendo o Vgs...")
        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_vgs = api.user_timeline(userID_vgs, 
                            since_id = last_seen_id_vgs,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_vgs):
                last_seen_id_vgs = retrieve_last_seen_id(file_name_vgs)
                if last_seen_id_vgs < mention.id:
                    last_seen_id_vgs = mention.id
                    store_last_seen_id(last_seen_id_vgs, file_name_vgs)

                    #Frases
                    arquivoFrases = open(frasestxt_vgs, 'r')
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
            
        

def store_tweets_vgs(): # Armazena os Tweets do Vgs
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_vgs = 5*60
        tempo_que_funciona =  time.time() + tempo_vgs
        last_seen_id_vgs = retrieve_last_seen_id(file_name_vgs)


        while time.time()<=tempo_que_funciona:
            time.sleep(6)
            mentions_vgs = api.user_timeline(userID_vgs, 
                           since_id = last_seen_id_vgs,
                           include_rt = False,
                           tweet_mode = 'extended') 
            for mention in reversed(mentions_vgs):
                print(str(mention.id) + ' - ' + mention.full_text, '- Vgs')
                last_seen_id_vgs = retrieve_last_seen_id(file_name_vgs)
                if last_seen_id_vgs < mention.id:
                    last_seen_id_vgs = mention.id
                    store_last_seen_id(last_seen_id_vgs, file_name_vgs)
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
    time.sleep(tempo_vgs)

p_store_tweets_vgs = threading.Thread(target=store_tweets_vgs)
p_reply_to_tweets_vgs = threading.Thread(target=reply_to_tweets_vgs)

