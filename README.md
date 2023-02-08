# Projetos de Python
O intuito destes projetos era majoritariamente aprender python e me familiarizar com bibliotecas. É mais um relato do que propriamente uma documentação do projeto.
<br>
<a href='https://github.com/dudrt/Twitter_Bot/edit/main/README.md#ex'>`Exchange_bot`</a>
<a href='https://github.com/dudrt/Twitter_Bot/edit/main/README.md#bot'>`Bot_Make_Art`</a>
<a href='https://github.com/dudrt/Twitter_Bot/edit/main/README.md#gato'>`Gatos_diarios`</a>

<hr>

## <div id="ex">Exchange Bot</div>

Este bot foi o primeiro que eu fiz e tinha como objetivo funcionar como um bot informativo.<br>
Todo os dias ao meio dia o bot postava a cotação atual do: <br>
• Dólar <br>
• Euro <br>
• Bitcoin <br>
• E através de Web Scraping, pegava a quantidade de imposto que o Brasil havia pago desde o começo do ano. <br>

Para este projeto usei as bibliotecas: <br>
• selenium <br>
• time <br>
• tweepy <br>
• os <br>
• datetime <br>

A ideia de usar o selenium foi por conta dele ser necessário para a obtenção dos dados de imposto, logo não acreditei ser preciso o uso de uma API para o restante. <br>

O projeto foi rodado e hospedado no <a href='https://replit.com/@EduardoRoth1'>Replit</a> , o site em si não possui um sistema grátis de hospedagem, porém sempre há um jeito.<br>
Rodando um pequeno script e com a ajuda do site <a href='https://uptimerobot.com'>UptimeRobot</a> , que é um serviço de monitoramento, é possivel deixar seu código rodando sem precisar ficar na página do código. Basicamente o site UptimeRobot fica mandando requests a cada certo tempo para o site que você deseja. Com isso, a página do replit é recarregada e o código, caso não estivesse rodando, era iniciado.<br>
Para este projeto usei as bibliotecas:<br>
import requests
import json
from replit import db
from translate import Translator
import random
import tweepy
import os
from datetime import datetime
import time
<hr>

## <div id="bot">Bot Make Art</div>
 Quando a primeira inteligência artifical que cria imagens a partir de palavras foi criada e disponibilizada, a primeira ideia que veio na minha cabeça foi criar um bot interativo capaz de aceitar entrada de dados.
 O <a href='https://github.com/dudrt/Twitter_Bot/blob/main/bot_make_art.py'>Bot Make Art</a> funcionava com as bibliotecas: <br>
• tweepy <br>
• urllib.request <br>
• io <br>
• openai <br>
• time <br>
• os <br>

E como foi hospedado no replit, também foi utilizado a própria biblioteca de banco de dados do site.<br>
• from replit import db <br>

A cada 5 segundos, o código fazia um request pegando os últimos 5 tweets que contiam a hastag `botmakeart`, dividia o tweet e pegava as palavras para transformar em imagem. 
O Bot tinha a capacidade de pegar qualquer mensagem pública que continha as palavras chave, independente se era um comentário, tweet, uma resposta de alguma publicação etc.
O código pegava as palavras chave e mandava para a biblioteca <a href='https://openai.com'>openai</a>, que é a biblioteca utilizada para fazer as requests dos serviços disponibilizados pela empresa.
Logo após, a foto é virtualmente salva e recebe um nome fake, para que seja possível posta-la.

<hr>

## <div id="gato">Gatos Diários</div>

Após acabar o tempo grátis de experiência da OpenAi, me veio a ideia de fazer um bot que usasse uma API, aí veio a ideia do <a href='https://github.com/dudrt/Twitter_Bot/blob/main/gatos_diarios.py'>Gatos Diários</a>.
Como o próprio nome já diz, um bot que fizesse requests para uma API de fotos de gato e poste uma foto todo dia. Único quesito diferente é que agora a imagem que foi requisitada é baixada e realmente salva.<br>

Códigos pequenos ,mas que me ajudaram a compreender melhor a linguagem e a lógica de programação.
