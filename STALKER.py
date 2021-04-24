#Funções Paralelas
'''
# Responde salve
from salve.func_salve import p_manda_salve
p_manda_salve.start()

# Trap
from trap.func_trap import p_tweet_trap
p_tweet_trap.start()

#Funções do Vgs
from vgs.func_vgs import p_store_tweets_vgs, p_reply_to_tweets_vgs
p_store_tweets_vgs.start()
p_reply_to_tweets_vgs.start()


#Funções do thu
from thu.func_thu import p_store_tweets_thu, p_reply_to_tweets_thu
p_store_tweets_thu.start()
p_reply_to_tweets_thu.start()

#Funções do lari
from lari.func_lari import p_store_tweets_lari, p_reply_to_tweets_lari
p_store_tweets_lari.start()
p_reply_to_tweets_lari.start()


#Funções do luiza
from luiza.func_luiza import p_store_tweets_luiza, p_reply_to_tweets_luiza
p_store_tweets_luiza.start()
p_reply_to_tweets_luiza.start()
'''
#Funções do thony
from thony.func_thony import p_store_tweets_thony, p_reply_to_tweets_thony
p_store_tweets_thony.start()
p_reply_to_tweets_thony.start()
