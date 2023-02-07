from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tweepy
import os
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

#-----------------------------------pegar dólar-----------------------
def infinity():
  driver.get("https://www.google.com.br/")
  pesquisar = driver.find_element(By.NAME, "q")
  pesquisar.send_keys("dólar para real")
  pesquisar.send_keys(Keys.ENTER)
  dolar = driver.find_element(By.CSS_SELECTOR, '[class="DFlfde SwHCTb"]');
  print(dolar.text)
  printdolar="💵DÓLAR R$:"+dolar.text;
#-----------------------------------fim pegar dólar-------------------
#-----------------------------------pegar euro------------------------
  driver.get("https://www.google.com.br/")
  pesquisar = driver.find_element(By.NAME, "q")
  pesquisar.send_keys("euro para real hoje")
  pesquisar.send_keys(Keys.ENTER)
  euro = driver.find_element(By.CSS_SELECTOR, '[class="DFlfde SwHCTb"]')
  print(euro.text)
  printeuro="💶EURO R$:"+euro.text;
#----------------------------------fim pegar euro------------------
#----------------------------------pegar bitcoin-------------------
  driver.get("https://www.google.com.br/")
  pesquisar = driver.find_element(By.NAME, "q")
  pesquisar.send_keys("bitcoin para real hoje")
  pesquisar.send_keys(Keys.ENTER)
  bitcoin = driver.find_element(By.CSS_SELECTOR, '[class="pclqee"]')
  print(bitcoin.text)
  printbit="💸BITCOIN R$:"+bitcoin.text;
#--------------------------------------fim pegar bitcoin-----------------
#--------------------------------------pegar imposto---------------------
  impostototal=[]
  impostoformat=[]
  nu=""
  driver.get("https://impostometro.com.br/")
  impost= driver.find_element(By.ID, "counterBrasil")
#--formatar o imposto--

  imposto=str(impost.text)
  tamanho=len(imposto)

  for i in range (tamanho):
    testenumero=imposto[i].isnumeric()
    if testenumero:
      impostototal.append(imposto[i])

  tamanhoimp=len(impostototal)
  local=tamanhoimp
  a=0

  while tamanhoimp >=1:
    a=a+1
    if a==4:
      impostoformat.insert(0,'.')
      a=0
    else:
      local=local-1
      impostoformat.insert(0,impostototal[local])
      tamanhoimp=tamanhoimp-1
        
  for n in impostoformat:
    nu+=n

  imp=nu.split('.');

  tamanho=len(imp)
  print (tamanho)
  if tamanho<5:
    nu+=".000"
#--fim formatar imposto--
      
  printimposto="💰Imposto 2022 R$"+nu
  
  token = os.environ['secret_token']
  secrettoken = os.environ['token']
  key = os.environ['key']
  secretkey = os.environ['secret_key']
  auth=tweepy.OAuthHandler(f"{key}",f"{secretkey}")
  auth.set_access_token(f"{token}",f"{secrettoken}")
  tweet=tweepy.API(auth)
  print(printdolar+'\n'+printeuro+'\n'+printbit+'\n'+printimposto)
  tweet.update_status(printdolar+'\n'+printeuro+'\n'+printbit+'\n'+printimposto)
#--------------------------------fim pegar imposto--------------------
#--------------------------------testar horario e postar--------------

def testeHorario():
  date = datetime.now()
  ag=str(date)
  val = ag.split(' ');
  hora = val[1].split(":")
  
  if hora[0] == '15' and hora[1] == "00":
    print(hora[0]+":"+hora[1])
    time.sleep(60)
    infinity()

rodar=True;
def temporizador():
  while rodar==True:
    time.sleep(60)
    testeHorario()

temporizador()
