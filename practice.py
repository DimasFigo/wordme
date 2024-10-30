import requests

api_key = 'a219c317-307a-4b58-bd87-4d1be14fa329'
word = 'Watermelon'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definition = res.json()
for definition in definition:
    print(definition)