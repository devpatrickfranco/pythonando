from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Pessoa, Token
from secrets import token_hex
from hashlib import sha256

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

def conecaoBanco():
    engine = create_engine('sqlite:///meu_banco.db', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post('/cadastro')
def cadastro(nome: str, email: str, senha: str):
    session = conecaoBanco()
    usuario = session.query(Pessoa).filter_by(email=email, senha=senha).all()
    
    if not usuario:
        senha = sha256(senha.encode()).hexdigest()
        novo_usuario = Pessoa(name=nome, email=email, senha=senha) 
        
        session.add(novo_usuario)
        session.commit()

        return {'msg': 'sucesso! usuario cadastrado'}

    return {'msg': 'usuario já cadastrado'}

@app.post('/login')
def login(email: str, senha: str):
    session = conecaoBanco()
    user = session.query(Pessoa).filter_by(email=email, senha=sha256(senha.encode()).hexdigest()).all()
    print(user)
    if not user:
        return {'msg': 'usuario não existe'}

    while True:
        token = token_hex(50)
        tokenExiste = session.query(Token).filter_by(token=token).all()

        if not tokenExiste:
            pessoaExiste = session.query(Token).filter_by(id_pessoa=user[0].id).all()
            
            if not pessoaExiste:
                novoToken = Token(id_pessoa=user[0].id, token=token)
                session.add(novoToken)
            else:
                pessoaExiste[0].token = token
                
            session.commit()
            break
    return token

if __name__ == '__main__':
    uvicorn.run('controller:app', port=5000, reload=True, access_log=True)