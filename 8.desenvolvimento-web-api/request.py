from fastapi import Body
import requests

response = requests.post(f"http://localhost:8000/usuarios", json={'id': 4, 'nome': 'João', 'senha': 'Hash256***'})
print(response.json())