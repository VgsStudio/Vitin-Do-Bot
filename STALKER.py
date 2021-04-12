import tweepy, time, random, threading
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

print('Bot da perfeição', flush=True)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Pessoas
    #Vitin
userID_vgs = 'vgs_studio'

mentions_vgs = api.user_timeline(userID_vgs, 
                           tweet_mode = 'extended'
                           )

file_name_vgs = 'last_seen_id_vgs.txt'
frasestxt_vgs = 'frases_vitin.txt'

    #Lulu   
userID_luiza = 'luizaskun'


mentions_luiza = api.user_timeline(userID_luiza, 
                           tweet_mode = 'extended'
                           )

file_name_luiza = 'last_seen_id_luiza.txt'
frasestxt_luiza = 'frases_luiza.txt'

    #Lari   
userID_lari = 'llaricasarini'

mentions_lari = api.user_timeline(userID_lari, 
                           tweet_mode = 'extended'
                           )

file_name_lari = 'last_seen_id_lari.txt'
frasestxt_lari = 'frases_lari.txt'


#Funções da Lari


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


def reply_to_tweets_lari(): # Responde o lari
    print('procurando uns tweets do lari', flush=True)
    while True:
        print("Reiniciando...")
        tempo_lari = 5*60 #5 minutos vezes 60
        time.sleep(tempo_lari)
        tempo_que_funciona = time.time() + tempo_lari #tempo de 5 minutos
        print("Respondendo o lari")
        while time.time() <= tempo_que_funciona:
            last_seen_id_lari = retrieve_last_seen_id_lari(file_name_lari)

            mentions_lari = api.user_timeline(userID_lari, 
                                since_id = last_seen_id_lari,
                                tweet_mode = 'extended')
            #Frases
            arquivoFrases = open(frasestxt_lari, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases

            for mention in reversed(mentions_lari):
                last_seen_id_lari = mention.id
                store_last_seen_id_lari(last_seen_id_lari, file_name_lari)

                api.update_status("@" + mention.user.screen_name + 
                                    (' %s' % frase), mention.id)

def store_tweets_lari(): # Armazena os Tweets do lari
    print('Armazenando uns tweets uns tweets', flush=True)
    while True:
        last_seen_id_lari = retrieve_last_seen_id_lari(file_name_lari)

        mentions_lari = api.user_timeline(userID_lari, 
                            since_id = last_seen_id_lari,
                            tweet_mode = 'extended')
        for mention in reversed(mentions_lari):
            print(str(mention.id) + ' - ' + mention.full_text)
            last_seen_id_lari = mention.id
            store_last_seen_id_lari(last_seen_id_lari, file_name_lari)

p_store_tweets_lari = threading.Thread(target=store_tweets_lari)
p_reply_to_tweets_lari = threading.Thread(target=reply_to_tweets_lari)

#Funções da Lulu

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


def reply_to_tweets_luiza(): # Responde o luiza
    print('procurando uns tweets do luiza', flush=True)
    while True:
        print("Reiniciando...")
        tempo_luiza = 5*60 #5 minutos vezes 60
        time.sleep(tempo_luiza)
        tempo_que_funciona = time.time() + tempo_luiza #tempo de 5 minutos
        print("Respondendo o luiza")
        while time.time() <= tempo_que_funciona:
            last_seen_id_luiza = retrieve_last_seen_id_luiza(file_name_luiza)

            mentions_luiza = api.user_timeline(userID_luiza, 
                                since_id = last_seen_id_luiza,
                                tweet_mode = 'extended')
            #Frases
            arquivoFrases = open(frasestxt_luiza, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases

            for mention in reversed(mentions_luiza):
                last_seen_id_luiza = mention.id
                store_last_seen_id_luiza(last_seen_id_luiza, file_name_luiza)

                api.update_status("@" + mention.user.screen_name + 
                                    (' %s' % frase), mention.id)

def store_tweets_luiza(): # Armazena os Tweets do luiza
    print('Armazenando uns tweets uns tweets', flush=True)
    while True:
        last_seen_id_luiza = retrieve_last_seen_id_luiza(file_name_luiza)

        mentions_luiza = api.user_timeline(userID_luiza, 
                            since_id = last_seen_id_luiza,
                            tweet_mode = 'extended')
        for mention in reversed(mentions_luiza):
            print(str(mention.id) + ' - ' + mention.full_text)
            last_seen_id_luiza = mention.id
            store_last_seen_id_luiza(last_seen_id_luiza, file_name_luiza)

p_store_tweets_luiza = threading.Thread(target=store_tweets_luiza)
p_reply_to_tweets_luiza = threading.Thread(target=reply_to_tweets_luiza)

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


def reply_to_tweets_vgs(): # Responde o Vitin
    print('procurando uns tweets do Vitin', flush=True)
    while True:
        print("Reiniciando...")
        tempo_vgs = 5*60 #5 minutos vezes 60
        time.sleep(tempo_vgs)
        tempo_que_funciona = time.time() + tempo_vgs #tempo de 5 minutos
        print("Respondendo o Vitin")
        while time.time() <= tempo_que_funciona:
            last_seen_id_vgs = retrieve_last_seen_id_vgs(file_name_vgs)

            mentions_vgs = api.user_timeline(userID_vgs, 
                                since_id = last_seen_id_vgs,
                                tweet_mode = 'extended')
            #Frases
            arquivoFrases = open(frasestxt_vgs, 'r')
            arrayFrases = arquivoFrases.read().split('\n')
            frase = random.choice(arrayFrases)
            #Frases

            for mention in reversed(mentions_vgs):
                last_seen_id_vgs = mention.id
                store_last_seen_id_vgs(last_seen_id_vgs, file_name_vgs)

                api.update_status("@" + mention.user.screen_name + 
                                    (' %s' % frase), mention.id)

def store_tweets_vgs(): # Armazena os Tweets do Vitin
    print('Armazenando uns tweets uns tweets', flush=True)
    while True:
        last_seen_id_vgs = retrieve_last_seen_id_vgs(file_name_vgs)

        mentions_vgs = api.user_timeline(userID_vgs, 
                            since_id = last_seen_id_vgs,
                            tweet_mode = 'extended')
        for mention in reversed(mentions_vgs):
            print(str(mention.id) + ' - ' + mention.full_text)
            last_seen_id_vgs = mention.id
            store_last_seen_id_vgs(last_seen_id_vgs, file_name_vgs)

p_store_tweets_vgs = threading.Thread(target=store_tweets_vgs)
p_reply_to_tweets_vgs = threading.Thread(target=reply_to_tweets_vgs)




#Funções Paralelas

#Funções do Vitin
p_store_tweets_vgs.start()
p_reply_to_tweets_vgs.start()

#Funções da Luiza
p_store_tweets_luiza.start()
p_reply_to_tweets_luiza.start()

#Funções da lari
p_store_tweets_lari.start()
p_reply_to_tweets_lari.start()
