import random
import requests

def generate_token():
    nr = random.randint(1, 999999999999999999999999999)
    nr1 = random.randint(1, 999999999999999999999999999)
    request_body = {
                    "clientName": "Alin Cernavoda",
                    "clientEmail": f"alin{nr}.cernavoda{nr1}@example.com"
                    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=request_body)
    # am generat token-ul si vrem sa il extragem din raspuns.
    # Observam ca raspunsul pe care l-am primit este un dictionar
    token = response.json()["accessToken"] # scriem .json() ca sa extragem tot raspunsul
    return token
