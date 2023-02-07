import requests
import json
from replit import db
from translate import Translator
import random
import tweepy
import os
from datetime import datetime
import time

#-------------------------------------------
key = os.environ['key']
secret_key = os.environ['secretkey']
token = os.environ['token']
secret_token = os.environ['secrettoken']
barrer = os.environ['barrer']

auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(token, secret_token)
bot = tweepy.API(auth)

client = tweepy.Client(f"{barrer}", f"{key}", f"{secret_key}", f"{token}",
                       f"{secret_token}")


#---------------------------------------------------
def post(url, texto):
  emoji_gato = ["😽", "😼", "😹", "😺", "😸", "🐱"]
  if (texto != ""):
    status = f"{texto} {emoji_gato[random.randint(0, 5)]}"
  else:
    status = f"Gato {emoji_gato[random.randint(0, 5)]}"
  print(url)
  data = requests.get(url).content
  f = open('img/imagem.jpg', 'wb')
  f.write(data)
  f.close()
  filename = 'img/imagem.jpg'

  bot.update_status_with_media(status, filename)

  print("Postado")


def request():
  url = "https://api.thecatapi.com/v1/images/search?limit=1"
  headers = {
    'x-api-key':
    'live_ascLj8ce25kmzAuN62c1JhQxz08eABvg2YZbtfcwV2tbIsI9P1gsjW66McLFzOPv'
  }
  igual = False

  response = requests.get(url, headers=headers)
  text = response.text
  print(text)
  data = json.loads(text)
  breeds = data[0]
  url = breeds["url"]
  id = breeds["id"]
  list = db["id"]

  for i in range(len(list)):
    if id == list[i]:
      igual = True

  if (igual == True):
    request()
  else:
    try:
      primeiro = data[0]["breeds"][0]["description"]
      translator = Translator(to_lang="pt")
      texto = translator.translate(primeiro)
      list.append(breeds["id"])
      db["id"] = list
      post(url, texto)
    except:
      list.append(breeds["id"])
      db["id"] = list
      texto = ""
      post(url, texto)


def timer():
  date = datetime.now()
  hora = date.hour
  minuto = date.minute
  print(f"{hora}:{minuto}")

  if (hora == 16 and minuto == 10):
    time.sleep(60)
    request()

rodar = True
while rodar:
  time.sleep(30)
  timer()
