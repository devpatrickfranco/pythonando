from dal import PessoaDal
from model import Pessoa

class PessoaController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) < 8 and (idade > 0 and idade < 200) and len(cpf) == 11:
            PessoaDal.salvar(Pessoa(nome, idade, cpf))
            return True
        return False

    @classmethod
    def allPeople(cls):
        return PessoaDal.ler()

    @classmethod
    def onePerson(cls, cpf: str):
        return PessoaDal.lerPessoa(cpf)