import oauth2
import urllib.parse
import json

class Twitter:

	def __init__(self, apiKey, apiKeySecret, tokenKey, tokenSecret):
		self.conexao(apiKey, apiKeySecret, tokenKey, tokenSecret)

	def conexao(self, apiKey, apiKeySecret, tokenKey, tokenSecret):
		self.consumer = oauth2.Consumer(apiKey,apiKeySecret)

		self.token = oauth2.Token(tokenKey,tokenSecret)

		self.cliente = oauth2.Client(self.consumer, self.token)

		return self.cliente

	def postarTweet(self, novoTweet):
		TextoCodificado = urllib.parse.quote(novoTweet, safe='')

		requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status='+TextoCodificado, method='POST')

		decoficar = requisicao[1].decode()
		requisicaoObj = json.loads(decoficar)
		
		return requisicaoObj

	def excluirTweet(self, id):
		requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/destroy/'+id+'.json', method="POST")

		decoficar = requisicao[1].decode()
		requisicaoObj = json.loads(decoficar)
		
		return requisicaoObj
	

	def pesquisar(self, pesquisa, lang):
		pesquisaCodificada = urllib.parse.quote(pesquisa, safe='')

		requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+pesquisaCodificada+'&lang='+lang)

		decoficar = requisicao[1].decode()

		requisicaoObj = json.loads(decoficar)
		tweets = requisicaoObj['statuses']

		return tweets