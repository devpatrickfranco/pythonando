from model import Produto
from model import *

class DaoCategoria:

    @classmethod
    def save(cls, categoria: Categoria):
        with open("categorias.txt", "a") as arq:
            arq.writelines(categoria)
            arq.writelines("\n")
    
    @classmethod
    def read(cls):
        with open("categorias.txt", "r") as arq:
            cls.categorias = arq.readlines()
        cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))
        
        cat = []
        for i in cls.categorias:
            cat.append(Categoria(i))
        
        return cat

class DaoVendas:
    
    @classmethod
    def save(cls, venda: Vendas):
        with open("vendas.txt", "a") as arq:
            arq.writelines(venda.itens_vendido.nome + "|" + 
                           venda.itens_vendido.preco + "|" + 
                           venda.itens_vendido.categoria + "|" +
                           venda.itens_vendido.vendedor + "|" + 
                           venda.itens_vendido.comprador + "|" +
                           str(venda.itens_vendido.qnt_vendida) + "|")
            arq.writelines('\n')
    
    @classmethod
    def read(cls):
        with open("venda.txt", "r") as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace("\n", ""), cls.venda))
        cls.venda = list(map(lambda x: x.split("|"), cls.venda))
        vendas = []
        for i in cls.venda:
            vendas.append(Venda(Produto(i[0], i[1], i[2], i[3], i[4], i[5], i[6])))
        return vendas

class DaoEstoque:
    @classmethod
    def save(cls, produto: Produto, quantidade):
        with open("estoque.txt", "a") as arq:
            arq.writelines(produto.nome + "|" + 
                           produto.preco + "|" + 
                           produto.categoria + "|" +
                           str(quantidade) + "|")
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open("estoque.txt", "r") as arq:
            cls.estoque = arq.readlines()
        cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
        cls.estoque = list(map(lambda x: x.split("|"), cls.estoque))
        estoque = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                estoque.append(Produto(i[0], i[1], i[2], i[3]))
        return estoque

class DaoFornecedor:
    @classmethod
    def save(cls, fornecedor: Fornecedor):
        with open("fornecedores.txt", "a") as arq:
            arq.writelines(fornecedor.nome + "|" + 
                           fornecedor.telefone + "|" + 
                           fornecedor.cnpj + "|" +
                           str(fornecedor.categoria) + "|")
            arq.writelines('\n')
    
    @classmethod
    def read(cls):
        with open("fornecedores.txt", "r") as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = list(map(lambda x: x.replace("\n", ""), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))
        fornecedores = []
        if len(cls.fornecedores) > 0:   
            for i in cls.fornecedores:
                fornecedores.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return fornecedores

class DaoPessoa:
    @classmethod
    def save(cls, pessoa: Pessoa):
        with open("cliente.txt", "a") as arq:
            arq.writelines(pessoa.nome + "|" + 
                           pessoa.telefone + "|" + 
                           pessoa.cpf + "|" +
                           str(pessoa.categoria) + "|")
            arq.writelines('\n')
        
    @classmethod
    def read(cls):
        with open("cliente.txt", "r") as arq:
            cls.clientes = arq.readlines()
        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))
        clientes = []
        if len(cls.clientes) > 0:   
            for i in cls.clientes:
                clientes.append(Pessoa(i[0], i[1], i[2], i[3]))
        return clientes

class DaoFuncionario:
    @classmethod
    def save(cls, funcionario: Funcionario):
        with open("funcionarios.txt", "a") as arq:
            arq.writelines(funcionario.nome + "|" + 
                           funcionario.telefone + "|" + 
                           funcionario.cpf + "|" +
                           str(funcionario.categoria) + "|")
            arq.writelines('\n')
    
    @classmethod
    def read(cls):
        with open("funcionarios.txt", "r") as arq:
            cls.funcionarios = arq.readlines()
        cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))
        funcionarios = []
        if len(cls.funcionarios) > 0:   
            for i in cls.funcionarios:
                funcionarios.append(Funcionario(i[0], i[1], i[2], i[3]))
        return funcionarios