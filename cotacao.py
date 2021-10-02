import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacao = json.loads(requisicao.text)

print('Cotação das moedas!')
print('Dólar: ',cotacao['USDBRL']['bid'])
print('Euro: ',cotacao['EURBRL']['bid'])
print('Bitcoin: ',cotacao['BTCBRL']['bid'])