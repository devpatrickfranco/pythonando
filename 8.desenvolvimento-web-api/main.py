from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Pessoa, Token
from secrets import token_hex

app = FastAPI()

def conecaoBanco():
    engine = create_engine('sqlite:///meu_banco.db', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post('/cadastro')
def cadastro(nome: str, user: str, senha: str):
    session = conecaoBanco()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()
    
    if not usuario:
        novo_usuario = Pessoa(name=nome, usuario=user, senha=senha) 
        
        session.add(novo_usuario)
        session.commit()

        return {'msg': 'sucesso! usuario cadastrado'}

    return {'msg': 'usuario já cadastrado'}

@app.post('/login')
def login(usuario: str, senha: str):
    session = conecaoBanco()
    user = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()
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