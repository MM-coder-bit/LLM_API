# Deploy de API Para Geração de Texto a Partir de Imagens com LLM
# Módulo Cliente

# Import
import requests

# URL da API
url = "http://localhost:3000/api"

# Payload (texto de entrada para o LLM)
#payload = {'text': (None, 'Which color is the car in the image?')}
#payload = {'text': (None, 'are there 9 birds in the picture?')}
#payload = {'text': (None, 'Which color is the elephant in the image?')}
payload = {'text': (None, 'What is the dog doing in the image?')}
#payload = {'text': (None, 'what animal is that in the picture?')}

# Imagem enviada para o modelo
#file = [('image', open('imagens//imagem1.png','rb'))]
#file = [('image', open('imagens//imagem2.png','rb'))]
file = [('image', open('imagens//imagem3.jpg','rb'))]
#file = [('image', open('imagens//cat.webp','rb'))]
#file = [('image', open('imagens//passaros.jpg','rb'))]

# Cabeçalho
headers = {'accept': 'application/json'}

# Faz a requisição à API e armazena a resposta
resposta = requests.request("POST", 
                            url, 
                            headers = headers, 
                            data = payload, 
                            files = file)

print(resposta.text)