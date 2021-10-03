import oauth2
import json
import urllib.parse

# Preencha as strings abaixo com seus dados da conta Twitter para Devs

apiKey = ''

apiKeySecret = ''

tokenKey = ''

tokenSecret = ''

consumer = oauth2.Consumer(apiKey,apiKeySecret)

token = oauth2.Token(tokenKey,tokenSecret)

cliente = oauth2.Client(consumer,token)

def Pesquisar(pesquisa):
	pesquisaCodificada = urllib.parse.quote(pesquisa, safe='')

	requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+pesquisaCodificada+'&lang=pt')

	decoficar = requisicao[1].decode()

	requisicaoObj = json.loads(decoficar)
	tweets = requisicaoObj['statuses']


	for tweet in tweets:
		print(tweet['user']['screen_name'])
		print(tweet['text'])
		print('')

def Postar(texto):
	TextoCodificado = urllib.parse.quote(texto, safe='')

	requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status='+TextoCodificado, method='POST')

	decoficar = requisicao[1].decode()
	requisicaoObj = json.loads(decoficar)
	return requisicaoObj['text']

print(Pesquisar('Python'))
print('__________________')
print(Postar('Dia inteiro mexendo com programação, foda'))
