from twitter import Twitter

# Acessar: https://developer.twitter.com/en/portal/dashboard e colocar os respectivos dados

apiKey = ''

apiKeySecret = ''

tokenKey = ''

tokenSecret = ''

twitter = Twitter(apiKey, apiKeySecret, tokenKey, tokenSecret)

'''postagem = twitter.postarTweet('Mensagem Random')

print(postagem)'''

'''pesquisa = twitter.pesquisar('Tokyo Revegers', 'pt')

for resultado in pesquisa:
	print(resultado['user']['screen_name'])
	print(resultado['text'])
	print('')'''

'''excluir = twitter.excluirTweet('1444400622757978113')
print(excluir)'''