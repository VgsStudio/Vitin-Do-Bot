import tweepy, time, random, threading, wikipedia

from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_page_sumarries(page_name):
    try:
        return [page_name, wikipedia.page(page_name).summary]
    except wikipedia.exceptions.DisambiguationError as e:
        return [[p, wikipedia.page(p).summary] for p in e.options]

def get_random_pages_summary(pages=0):
    wikipedia.set_lang("pt")
    ret = []
    page_names = [wikipedia.random(1) for i in range(pages)]
    for p in page_names:
        for page_summary in get_page_sumarries(p):
            ret.append(page_summary)
    return  ret


def random_page():
    while True:
        time.sleep(7*60) #15 min
        text = get_random_pages_summary(1)
        titulo = text[0]
        text = text[1]
        
        print('''%s
%s''' % (titulo, text)) # Frase postada
        try:
            api.update_status('''%s
%s''' % (titulo, text)) # Tweetar frase
        except:
            print('Grande Demais')             


p_random_page = threading.Thread(target=random_page)


