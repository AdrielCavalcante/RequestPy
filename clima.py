# Ideia de projeto, pegar api do tradutor e por em portugues
import requests
import json

cidade = 'Rio de janeiro'

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=29a246b1b59f2718d4e4c81c23a8e5a9')

clima = json.loads(requisicao.text)

print(f'{cidade} weather')
print("Weather condition:", clima['weather'][0]['main'])
print("Temperature:", round(float(clima['main']['temp']) - 273.15 , 2), "°C")