from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itens_vendido: Produto, vendedor, comprador, qnt_vendida, data=datetime.now()):
        self.itens_vendido = itens_vendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.qnt_vendida = qnt_vendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, telefone, cnpj, categoria: Categoria):
        self.nome = nome
        self.telefone = telefone
        self.cnpj = cnpj
        self.categoria = categoria

class Pessoa:
    def __init_(self, nome, telefone, email, cpf, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, email, cpf, endereco):
        super(Funcionario, self).__init__(nome, telefone, email, cpf, endereco)
        self.clt = clt
    