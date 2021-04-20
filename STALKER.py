import tweepy, time, random, threading
from os import environ


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


print('Vitin do Bot', flush=True)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

data = api.rate_limit_status()
print (data['resources']['statuses']['/statuses/user_timeline'])


    #Vitin
userID_vgs = 'vgs_studio'

file_name_vgs = 'last_seen_id_vgs.txt'
frasestxt_vgs = 'frases_vitin.txt'

    #Lari
userID_lari = 'llaricasarini'

file_name_lari = 'last_seen_id_lari.txt'
frasestxt_lari = 'frases_lari.txt'

    #luiza
userID_luiza = 'luizaskun'

file_name_luiza = 'last_seen_id_luiza.txt'
frasestxt_luiza = 'frases_luiza.txt'

    #thony
userID_thony = 'sanickBR'

file_name_thony = 'last_seen_id_thony.txt'
frasestxt_thony = 'frases_thony.txt'

    #thu
userID_thu = 'tutu_kosinski'

file_name_thu = 'last_seen_id_thu.txt'
frasestxt_thu = 'frases_thu.txt'


#Funções da thu-----------------------------------

def retrieve_last_seen_id_thu(file_name_thu):
    f_read = open(file_name_thu, 'r')
    last_seen_id_thu = int(f_read.read().strip())
    f_read.close()
    return last_seen_id_thu

def store_last_seen_id_thu(last_seen_id_thu, file_name_thu):
    f_write = open(file_name_thu, 'w')
    f_write.write(str(last_seen_id_thu))
    f_write.close()
    return

 
def reply_to_tweets_thu(): # Responde a thu
    print('Procurando uns tweets da thu...', flush=True)
    while True:
        tempo_thu = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_thu)
        tempo_que_funciona = time.time() + tempo_thu #tempo de 5 minutos
        last_seen_id_thu = retrieve_last_seen_id_thu(file_name_thu)
        
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
                store_last_seen_id_thu(last_seen_id_thu, file_name_thu)
                if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                    api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

def store_tweets_thu(): # Armazena os Tweets do thu
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_thu = 5*60
        tempo_que_funciona =  time.time() + tempo_thu
        last_seen_id_thu = retrieve_last_seen_id_thu(file_name_thu)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_thu = api.user_timeline(userID_thu, 
                           since_id = last_seen_id_thu,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_thu):
                print(str(mention.id) + ' - ' + mention.full_text,'- thu')
                last_seen_id_thu = mention.id
                store_last_seen_id_thu(last_seen_id_thu, file_name_thu)
    time.sleep(tempo_thu)


p_store_tweets_thu = threading.Thread(target=store_tweets_thu)
p_reply_to_tweets_thu = threading.Thread(target=reply_to_tweets_thu)




#Funções da thony-----------------------------------

def retrieve_last_seen_id_thony(file_name_thony):
    f_read = open(file_name_thony, 'r')
    last_seen_id_thony = int(f_read.read().strip())
    f_read.close()
    return last_seen_id_thony

def store_last_seen_id_thony(last_seen_id_thony, file_name_thony):
    f_write = open(file_name_thony, 'w')
    f_write.write(str(last_seen_id_thony))
    f_write.close()
    return

 
def reply_to_tweets_thony(): # Responde a thony
    print('Procurando uns tweets da thony...', flush=True)
    while True:
        tempo_thony = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_thony)
        tempo_que_funciona = time.time() + tempo_thony #tempo de 5 minutos
        last_seen_id_thony = retrieve_last_seen_id_thony(file_name_thony)
        
        print("Respondendo a thony...")
        while time.time() <= tempo_que_funciona:
            
            time.sleep(6)
            mentions_thony = api.user_timeline(userID_thony, 
                            since_id = last_seen_id_thony,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_thony):
                if last_seen_id_thony < mention.id:
                    last_seen_id_thony = mention.id
                    store_last_seen_id_thony(last_seen_id_thony, file_name_thony)

                    #Frases
                    arquivoFrases = open(frasestxt_thony, 'r')
                    arrayFrases = arquivoFrases.read().split('\n')
                    frase = random.choice(arrayFrases)
                    #Frases

                    if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                        api.create_favorite(mention.id)
                        api.retweet(mention.id)
                        api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)
                else:
                    break

def store_tweets_thony(): # Armazena os Tweets do thony
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_thony = 5*60
        tempo_que_funciona =  time.time() + tempo_thony
        last_seen_id_thony = retrieve_last_seen_id_thony(file_name_thony)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_thony = api.user_timeline(userID_thony, 
                           since_id = last_seen_id_thony,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_thony):
                print(str(mention.id) + ' - ' + mention.full_text,'- thony')
                if last_seen_id_thony < mention.id:
                    last_seen_id_thony = mention.id
                    store_last_seen_id_thony(last_seen_id_thony, file_name_thony)

                    last_seen_id_thony = mention.id
                    store_last_seen_id_thony(last_seen_id_thony, file_name_thony)
                    if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                        try:
                            api.create_favorite(mention.id)
                            api.retweet(mention.id)
                        except tweepy.TweepError as error:
                                    if error.api_code == 139:
                                        print('Tweet já favoritado...')
                        
                else:
                    break
    time.sleep(tempo_thony)




p_store_tweets_thony = threading.Thread(target=store_tweets_thony)
p_reply_to_tweets_thony = threading.Thread(target=reply_to_tweets_thony)




#Funções da luiza-----------------------------------

def retrieve_last_seen_id_luiza(file_name_luiza):
    f_read = open(file_name_luiza, 'r')
    last_seen_id_luiza = int(f_read.read().strip())
    f_read.close()
    return last_seen_id_luiza

def store_last_seen_id_luiza(last_seen_id_luiza, file_name_luiza):
    f_write = open(file_name_luiza, 'w')
    f_write.write(str(last_seen_id_luiza))
    f_write.close()
    return

 
def reply_to_tweets_luiza(): # Responde a luiza
    print('Procurando uns tweets da luiza...', flush=True)
    while True:
        tempo_luiza = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_luiza)
        tempo_que_funciona = time.time() + tempo_luiza #tempo de 5 minutos
        last_seen_id_luiza = retrieve_last_seen_id_luiza(file_name_luiza)
        
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
                store_last_seen_id_luiza(last_seen_id_luiza, file_name_luiza)
                if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                    api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

def store_tweets_luiza(): # Armazena os Tweets do luiza
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_luiza = 5*60
        tempo_que_funciona =  time.time() + tempo_luiza
        last_seen_id_luiza = retrieve_last_seen_id_luiza(file_name_luiza)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_luiza = api.user_timeline(userID_luiza, 
                           since_id = last_seen_id_luiza,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_luiza):
                print(str(mention.id) + ' - ' + mention.full_text,'- luiza')
                last_seen_id_luiza = mention.id
                store_last_seen_id_luiza(last_seen_id_luiza, file_name_luiza)
    time.sleep(tempo_luiza)


p_store_tweets_luiza = threading.Thread(target=store_tweets_luiza)
p_reply_to_tweets_luiza = threading.Thread(target=reply_to_tweets_luiza)


#Funções da lari-----------------------------------

def retrieve_last_seen_id_lari(file_name_lari):
    f_read = open(file_name_lari, 'r')
    last_seen_id_lari = int(f_read.read().strip())
    f_read.close()
    return last_seen_id_lari

def store_last_seen_id_lari(last_seen_id_lari, file_name_lari):
    f_write = open(file_name_lari, 'w')
    f_write.write(str(last_seen_id_lari))
    f_write.close()
    return

 
def reply_to_tweets_lari(): # Responde a lari
    print('Procurando uns tweets da lari...', flush=True)
    while True:
        tempo_lari = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_lari)
        tempo_que_funciona = time.time() + tempo_lari #tempo de 5 minutos
        last_seen_id_lari = retrieve_last_seen_id_lari(file_name_lari)
        
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
                store_last_seen_id_lari(last_seen_id_lari, file_name_lari)
                if 'RT @' not in mention.full_text: #Evita responder RTs sem comentários
                   api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

def store_tweets_lari(): # Armazena os Tweets do lari
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_lari = 5*60
        tempo_que_funciona =  time.time() + tempo_lari
        last_seen_id_lari = retrieve_last_seen_id_lari(file_name_lari)


        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_lari = api.user_timeline(userID_lari, 
                           since_id = last_seen_id_lari,
                           include_rt = False,
                           tweet_mode = 'extended') 

            for mention in reversed(mentions_lari):
                print(str(mention.id) + ' - ' + mention.full_text,'- Lari')
                last_seen_id_lari = mention.id
                store_last_seen_id_lari(last_seen_id_lari, file_name_lari)
    time.sleep(tempo_lari)


p_store_tweets_lari = threading.Thread(target=store_tweets_lari)
p_reply_to_tweets_lari = threading.Thread(target=reply_to_tweets_lari)

#Funções do Vitin-----------------------------------

def retrieve_last_seen_id_vgs(file_name_vgs):
    f_read = open(file_name_vgs, 'r')
    last_seen_id_vgs = int(f_read.read().strip())
    f_read.close()
    return last_seen_id_vgs

def store_last_seen_id_vgs(last_seen_id_vgs, file_name_vgs):
    f_write = open(file_name_vgs, 'w')
    f_write.write(str(last_seen_id_vgs))
    f_write.close()
    return

 
def reply_to_tweets_vgs(): # Responde o Vgs
    print('Procurando uns tweets do Vgs...', flush=True)
    while True:
        tempo_vgs = 5*60 #5 minutos -> 5 segundos * 60
        time.sleep(tempo_vgs)
        tempo_que_funciona = time.time() + tempo_vgs #tempo de 5 minutos
        last_seen_id_vgs = retrieve_last_seen_id_vgs(file_name_vgs)
        
        print("Respondendo o Vgs...")
        while time.time() <= tempo_que_funciona:
            time.sleep(6)
            mentions_vgs = api.user_timeline(userID_vgs, 
                            since_id = last_seen_id_vgs,
                            include_rt = False,
                            tweet_mode = 'extended')
            
            for mention in reversed(mentions_vgs):
                last_seen_id_vgs = retrieve_last_seen_id_vgs(file_name_vgs)
                if last_seen_id_vgs < mention.id:
                    last_seen_id_vgs = mention.id
                    store_last_seen_id_vgs(last_seen_id_vgs, file_name_vgs)

                    #Frases
                    arquivoFrases = open(frasestxt_vgs, 'r')
                    arrayFrases = arquivoFrases.read().split('\n')
                    frase = random.choice(arrayFrases)
                    #Frases

                    if ('RT @' not in mention.full_text): #Evita responder RTs sem comentários
                        api.create_favorite(mention.id)
                        api.retweet(mention.id)                    
                        api.update_status("@" + mention.user.screen_name + (' %s' % frase), mention.id)

                else:
                    break

                print("Parando de responder.")
            
        

def store_tweets_vgs(): # Armazena os Tweets do Vgs
    print('Armazenando uns tweets...', flush=True)
    while True:
        tempo_vgs = 5*60
        tempo_que_funciona =  time.time() + tempo_vgs
        last_seen_id_vgs = retrieve_last_seen_id_vgs(file_name_vgs)


        while time.time()<=tempo_que_funciona:
            time.sleep(6)
            mentions_vgs = api.user_timeline(userID_vgs, 
                           since_id = last_seen_id_vgs,
                           include_rt = False,
                           tweet_mode = 'extended') 
            for mention in reversed(mentions_vgs):
                print(str(mention.id) + ' - ' + mention.full_text, '- Vgs')
                last_seen_id_vgs = retrieve_last_seen_id_vgs(file_name_vgs)
                if last_seen_id_vgs < mention.id:
                    last_seen_id_vgs = mention.id
                    store_last_seen_id_vgs(last_seen_id_vgs, file_name_vgs)
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

#Responder salve

file_name_salve = 'last_salve_id.txt'

def retrieve_last_seen_id_salve(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id_salve(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def manda_salve():
    print('Respondendo salve...', flush=True)
    
    while True:
        time.sleep(10)

        last_seen_id_salve = retrieve_last_seen_id_salve(file_name_salve)
        
        mentions = api.mentions_timeline(
                                since_id = last_seen_id_salve,
                                tweet_mode='extended')
            
        for mention in reversed(mentions):
            print(str(mention.id) + ' - ' + mention.full_text)
            last_seen_id_salve = mention.id
            store_last_seen_id_salve(last_seen_id_salve, file_name_salve)
            
            if 'salve' in mention.full_text.lower():
                try:
                    print("Salve, cachorro do mangue")
                    api.update_status("@" + mention.user.screen_name + 
                                    " Salve, cachorro do mangue!", mention.id)
                except tweepy.TweepError as error:
                    if error.api_code == 187:
                        print('Erro: Salve já enviado!')  

p_manda_salve = threading.Thread(target = manda_salve)

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

#Funções Paralelas

# Responde salve
p_manda_salve.start()

# Trap
p_tweet_trap.start()

#Funções do Vgs
p_store_tweets_vgs.start()
p_reply_to_tweets_vgs.start()

#Funções da lari
p_store_tweets_lari.start()
p_reply_to_tweets_lari.start()

#Funções da luiza
p_store_tweets_luiza.start()
p_reply_to_tweets_luiza.start()

#Funções do thony
p_store_tweets_thony.start()
p_reply_to_tweets_thony.start()

#Funções da thu
p_store_tweets_thu.start()
p_reply_to_tweets_thu.start()


