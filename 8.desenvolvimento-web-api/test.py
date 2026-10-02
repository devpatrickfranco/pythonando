from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str
    email: Optional[str]


lista = [
    Usuario(id=1, nome='Patrick', senha='Hash256***'),
    Usuario(id=2, nome='Laura', senha='Hash256***'),
    Usuario(id=3, nome='Luzia', senha='Hash256***')
]

@app.post("/usuarios")
def criar_usuarios(user: Usuario):
    lista.append(user)
    return {"status":"200", "msg": "usuario criado"}

@app.get("/usuarios/all")
def listar_usuarios(    ):
    return {"status": 200, "lista": lista}


"""
@app.get("/usuario/{id}")
def main(id: int):
    for i in usuarios:
        if i[0] == id:
            return i
        else:
            return {"error": "Usuário não encontrado"}

@app.post("/usuario")
def create_usuario(nome: str, email: str):
    for i in usuarios:
        if i[2] == email:
            return {'error': 'esse email já existe'}
    novoId = i[0] + 1
    usuarios.append((novoId, nome, email))
    #print(usuarios)
    return {'msg': 'usuario criado com sucesso'}
"""