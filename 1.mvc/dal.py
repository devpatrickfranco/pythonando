from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as arquivo:
            arquivo.write(f"{pessoa.nome},{str(pessoa.idade)},{pessoa.cpf}\n")

    @classmethod
    def ler(cls):
        with open('pessoas.txt', 'r') as arquivo:
            print(arquivo.read())

    @classmethod
    def lerPessoa(cls, cpf: str):
        with open('pessoas.txt', 'r') as arquivo:
            for linha in arquivo:
                pessoa = linha.strip().split(',')
                if pessoa[2] == cpf:
                    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Cpf: {pessoa[2]}")
                    return
        print('Pessoa nao encontrada')