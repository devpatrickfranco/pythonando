from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Todo(BaseModel):
    tarefa: str
    concluida: bool
    prazo: Optional[date]

lista = []

app = FastAPI()

@app.post('/criar')
def criar_tarefa(todo: Todo):
    try:
        lista.append(todo)
        return {'status': 'sucesso'}
    except:
        return {'status': 'error'}

@app.post('/concluir/{id}')
def concluir_tarefa(id: int):
    try:
        lista[id].concluida = not lista[id].concluida
        return {'status': 'sucesso, tarefa concluida!'}
    except:
        return {'status': 'error'}


@app.post('/listar')
def listar_tarefas(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.concluida == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.concluida == True, lista))

@app.get('/listar/{id}')
def listar_tarefa(id: int):
    try:
        return lista[id]    
    except:
        return {'status': 'error, tarefa não existe'}

@app.post('/deletar')
def deletar_tarefa(id: int):
    try: 
        del lista[id]
        return {'status': "tarefa deletada com sucesso!"}
    except: 
        return {'status': 'error'}