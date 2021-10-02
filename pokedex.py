import requests
import json

try:
    # Para o website saber de onde eu vim
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    
    req = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151', headers=headers, timeout=5, allow_redirects = True)
    
    pokedex = json.loads(req.text)

    print('Pokedex Kanto:')
    for i in range(151):
        print(i+1,": ",pokedex['results'][i]['name'])

except Exception as err:
    print('Erro na conexão: ', err)
    

