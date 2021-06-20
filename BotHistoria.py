# -*- coding: utf-8 -*-
import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
# consumer_key, consumer_secret
# etapa de autenticação. Essas chaves são obtidas dentro do Twitter Deveolper, "API Key" e "API Key Secret"

auth.set_access_token('key', 'secret')
#key, secret

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# esses dois parâmetros é só para executar depois que o limite dos tweets for atingido

user = api.me()

print(user)

search = 'a história vai cobrar'
numero = 30

for tweet in tweepy.Cursor(api.search, search).items(numero):
  try:
    print("nome do usuário: @", tweet.user.screen_name)
    api.update_status(status='@' + tweet.user.screen_name + " Ustra morreu de velho.")
    print('Tweet enviado corretamente')
    time.sleep(30)
  except tweepy.TweepError as error:
    print(error.reason)
  except StopIteration:
    break
