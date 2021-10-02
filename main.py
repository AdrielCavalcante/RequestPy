import requests

try:
    requisicao = requests.get('https://api.github.com/users/adrielcavalcante')
    print(requisicao)
except Exception as err:
    print('Erro: ',err)


