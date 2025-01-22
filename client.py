import requests

url = 'http://127.0.0.1:5004/check_grammar'

data = {
    'sentence': "grammar:The ball is being throwning by her"   #"grammar: she has eat apples"  #"The man is bite by the dog"              #"grammar: The ball is being throwning by her"    #"grammar: This sentences, has bads grammar and spelling!"
}

response = requests.post(url, json=data)

print(response.json())
