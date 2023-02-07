import tweepy
import urllib.request
import io
import openai
import time
import os
from keep_alive import keep_alive
from replit import db
# -----------------------Tweepy Login-------------------
key = os.environ['key']
secretkey = os.environ['secret_key']
token = os.environ['acces_token']
secrettoken = os.environ['secret_token']
barrer = os.environ['barrer']
auth = tweepy.OAuthHandler(f"{key}", f"{secretkey}")
auth.set_access_token(f"{token}", f"{secrettoken}")
bot = tweepy.API(auth)

client=tweepy.Client(f"{barrer}",f"{key}",f"{secretkey}",f"{token}",f"{secrettoken}")
# ------------------------------------------------------
# -----------------------OpenIa Login-------------------
dalle = os.environ['dall-e']
openai.api_key = f"{dalle}"

# ------------------------------------------------------
def repost():
  testando = bot.search_tweets(q='#botmakeart', count=5, result_type='recent')
  print("----------------------------------")
  global id
  global ultima_pessoa
  id=testando[0].id
  ultima_pessoa = db["last"]
  if '#botmakeart' in testando[0].text:
    if testando[0].user.screen_name == ultima_pessoa:
      print(f'já foi {ultima_pessoa}')
      return
    else:
      db["last"] = testando[0].user.screen_name
      pegar_palavras(testando[0].text, testando[0].user.screen_name)


def pegar_palavras(palavra, pessoa):
  trans_image = palavra.split('#botmakeart')
  pedido = trans_image[1]
  pedido_separado = pedido.split(" ")
  tags = ''
  for i in range(len(pedido_separado)):
    if (pedido_separado[i] != ""):
      tags = f"{tags}#{pedido_separado[i]} "

  post_image(pedido, tags, pessoa)


## -----------------------Post Image--------------------
def post_image(pedido, tags, pessoa):
  try:
    response = openai.Image.create(prompt=pedido, n=1, size="512x512")
    image_url = response['data'][0]['url']
    print(image_url)
    text = f"#dalle #dalle2 #freetouse\n@{pessoa}\ntags:{tags}\n"
    print(text)
    data = urllib.request.urlopen(image_url).read()
    file_like_object = io.BytesIO(data)
    bot.update_status_with_media(text, 'fake_name.jpg', file=file_like_object)
    like_tweet()
  except:
    print("erro")
  
def like_tweet():
  print(id)
  client.like(id)
# ------------------------------------------------------
while (True):
  repost()
  time.sleep(5)
