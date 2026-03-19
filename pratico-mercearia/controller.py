from model import Categoria, Produto, Venda, Estoque, Fornecedor, Pessoa
from dal import DaoCategoria, DaoEstoque, DaoVendas, DaoPessoa, DaoFornecedor
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, categoria):
        existe = False
        x = DaoCategoria().read()
        for i in x:
            if i.categoria == categoria:
                existe = True
        if not existe:
            DaoCategoria().save(categoria)
            print("Categoria cadastrada com sucesso")
        else:
            print("Categoria ja cadastrada")

    def removerCategoria(self, categoria):
        x = DaoCategoria().read()
        cat = list(filter(lambda x: x.categoria == categoria, x))
        if cat:
            for i in range(len(x)):
                if x[i].categoria == categoria:
                    del x[i]
                    break
            print("Categoria removida com sucesso")
        else:
            print("Categoria nao encontrada")
        
        with open("categorias.txt", "w") as arq:
            for i in x:
                arq.writelines(f"{i.categoria}\n")
        
        estoque = DaoEstoque().read()
        estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, "SEM CATEGORIA"), x.quantidade)
                            if(x.produto.categoria == categoria) else (x), estoque
                            ))            
        with open("estoque.txt", "w") as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + " | " + 
                str(i.produto.preco) + " | " + 
                i.produto.categoria + " | " +
                str(i.quantidade) + " | ")
                arq.writelines('\n')

    def alterarCategoria(self, categoria, novaCategoria):
        x = DaoCategoria().read()
        cat = list(filter(lambda x: x.categoria == categoria, x))
        
        if cat:
            cat1 = list(filter(lambda x: x.categoria == novaCategoria, x))
            if len(cat1) == 0:
                
                def alterar(x):
                    if x.categoria == categoria:
                        x.categoria = novaCategoria
                    return x
                x = list(map(alterar, x))
                print("Categoria alterada com sucesso")
            else:
                print("Nova categoria ja cadastrada")
        else:
            print("Categoria a ser modificada nao encontrada")        
        
        with open("categorias.txt", "w") as arq:
            for i in x:
                arq.writelines(f"{i.categoria}\n") 

        estoque = DaoEstoque().read()
        estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, novaCategoria), x.quantidade)
                            if(x.produto.categoria == categoria) else (x), estoque
                            ))
        with open("estoque.txt", "w") as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + " | " + 
                str(i.produto.preco) + " | " + 
                i.produto.categoria + " | " +
                str(i.quantidade) + " | ")
                arq.writelines('\n')


    def mostrarCategorias(self):
        x = DaoCategoria().read()
        if x:
            for i in x:
                print(f"Categoria: {i.categoria}")    
        else:
            print("Nenhuma categoria cadastrada")

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque().read()
        y = DaoCategoria().read()
        h = list(filter(lambda x: x.categoria == categoria, y))
        estoq = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(estoq) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque().save(produto, quantidade)
                print("Produto cadastrado com sucesso")
            else:
                print("Produto ja cadastrado")
        else:
            print("Categoria nao encontrada")
    
    def removerProduto(self, nome):
        x = DaoEstoque().read()
        prod = list(filter(lambda x: x.produto.nome == nome, x))
        if prod:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print("Produto removido com sucesso")
        else:
            print("Produto nao encontrado")

        with open("estoque.txt", "w") as arq:
            for i in x:
                arq.writelines(i.produto.nome + " | " + 
                str(i.produto.preco) + " | " + 
                i.produto.categoria + " | " +
                str(i.quantidade) + " | ")
                arq.writelines('\n')
    
    
    def alterarProduto(self, nome, novoNome, novoPreco, novaQuantidade, novaCateogoria):
        x = DaoEstoque().read()
        y = DaoCategoria().read()
        h = list(filter(lambda x: x.categoria == novaCateogoria, y))
        if h:
            estoq = list(filter(lambda x: x.produto.nome == nome, x))
            
            if estoq:
                nomeJaExiste = list(filter(lambda x: x.produto.nome == novoNome, x))
                if not nomeJaExiste:
                    def alterar(x):
                        if x.produto.nome == nome:
                            x.produto.nome = novoNome
                            x.produto.preco = novoPreco
                            x.produto.categoria = novaCateogoria
                            x.quantidade = novaQuantidade
                        return x
                    x = list(map(alterar, x))
                    print("Produto alterado com sucesso")
                else:
                    print("Nome desejado já cadastrado")
            else:
                print("O Produto informado para alteração não existe")
            
            with open("estoque.txt", 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + " | " + 
                    str(i.produto.preco) + " | " + 
                    i.produto.categoria + " | " +
                    str(i.quantidade) + " | ")
                    arq.writelines('\n')
        else:
            print("A cateogira informada não existe")

    def mostrarEstoque(self):
        x = DaoEstoque().read()
        if x:
            for i in x:
                print(f"Produto: {i.produto.nome} | Preço: {i.produto.preco} | Categoria: {i.produto.categoria} | Quantidade: {i.quantidade}")
        else:
            print("Nenhum produto cadastrado")

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque().read()
        temp = []
        exist = False
        quant_suficiente = False
        
        for i in x:
            if i.produto.nome == nomeProduto:
                exist = True
                if i.quantidade >= quantidadeVendida:
                    quant_suficiente = True
                    i.quantidade = int(i.quantidade) - int(quantidadeVendida)
        
                    vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                    valorTotal = int(i.produto.preco) * int(quantidadeVendida)
                    DaoVendas.save(vendido)

            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open("estoque.txt", "w")
        arq.write("")

        for i in temp:
            with open("estoque.txt", "a") as arq:
                arq.writelines(i[0].nome + " | " + 
                str(i[0].preco) + " | " + 
                i[0].categoria + " | " +
                str(i[1]) + " | ")
                arq.writelines('\n')

        if not exist:
            print("Produto nao encontrado")
        elif not quant_suficiente:
            print("Quantidade insuficiente")
        else:
            print("Venda realizada com sucesso")
            return valorTotal

    def relatorioVendas(self):
        vendas = DaoVendas().read()
        produtos = []
        for i in vendas:
            nome = i.itens_vendido.nome
            quantidade = i.qnt_vendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': x['quantidade'] + quantidade}
                if (x['produto']) == nome else(x), produtos))
            else:
                produtos.append({"produto": nome, "quantidade": quantidade})

        ordenada = sorted(produtos, key=lambda k: k["quantidade"], reverse=True)
        print("Produtos mais vendidos: ")
        for i in ordenada:
            print(f"Produto: {i['produto']} | Quantidade: {i['quantidade']}")    

    def mostrarVenda(self, dataInicio, dataFim):
        vendas = DaoVendas().read()
        dataInicio = datetime.strptime(dataInicio, "%d/%m/%Y")
        dataFim = datetime.strptime(dataFim, "%d/%m/%Y")
        
        vendasSelecionados = list(filter(lambda x: x.data >= dataInicio 
                                        and x.data <= dataFim, vendas))
        
        cont = 1
        total = 0

        for i in vendasSelecionados:
            print(f"Venda {cont}")
            print(f"Produto: {i.itens_vendido.nome}")
            print(f"Categoria: {i.itens_vendido.categoria}")
            print(f"Preço: {i.itens_vendido.preco}")
            print(f"Vendedor: {i.vendedor}")
            print(f"Comprador: {i.comprador}")
            print(f"Quantidade: {i.qnt_vendida}")
            print(f"Data: {i.data}")
            print("-" * 20)
            cont += 1
            total += int(i.itens_vendido.preco) * int(i.qnt_vendida)
        
        print(f"Total Geral: {total}")

class ControllerFornecer:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor().read()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(listaCnpj) > 0 or len(listaTelefone) > 0:
            print("Fornecedor já cadastrado")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                y = DaoCategoria().read()
                h = list(filter(lambda x: x.categoria == categoria, y))
                if h:
                    fornecedor = Fornecedor(nome, telefone, cnpj, categoria)
                    DaoFornecedor.save(fornecedor)
                    print("Fornecedor cadastrado com sucesso")
                else:
                    print("Categoria informada não existe")
            else:
                print("Digite dados validos, verifique o CNPJ ou o Telefone")

    def editarFornecedor(self, nomeAntigo, nomeNovo, cnpjNovo, telefoneNovo, categoriaNova):
        x = DaoFornecedor().read()
        listaNome = list(filter(lambda x: x.nome == nomeAntigo, x))
        listaCnpj = list(filter(lambda x: x.cnpj == cnpjNovo, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefoneNovo, x))

        if len(listaNome) > 0:
            if len(listaCnpj) == 0 and len(listaTelefone) == 0:
                if len(cnpjNovo) == 14 and len(telefoneNovo) <= 11 and len(telefoneNovo) >= 10:
                    y = DaoCategoria().read()
                    h = list(filter(lambda x: x.categoria == categoriaNova, y))
                    if h:
                        fornecedor = Fornecedor(nomeNovo, telefoneNovo, cnpjNovo, categoriaNova)
                        x = list(filter(lambda x: x.nome != nomeAntigo, x))
                        with open('fornecedores.txt', 'w') as arq:
                            for i in x:
                                arq.write(i.nome + " | " + i.telefone + " | " + i.cnpj + " | " + i.categoria + "\n")
                        DaoFornecedor.save(fornecedor)
                        print("Fornecedor editado com sucesso")
                    else:
                        print("Categoria informada não existe")
                else:
                    print("Digite dados validos, verifique o CNPJ ou o Telefone")
            else:
                print("Fornecedor já cadastrado")
        else:
            print("Fornecedor não encontrado")
    
    def removerFornecedor(self, nome):
        x = DaoFornecedor().read()
        listaNome = list(filter(lambda x: x.nome == nome, x))
        if len(listaNome) > 0:
            x = list(filter(lambda x: x.nome != nome, x))
            with open('fornecedores.txt', 'w') as arq:
                for i in x:
                    arq.write(i.nome + " | " + i.telefone + " | " + i.cnpj + " | " + i.categoria + "\n")
            print("Fornecedor removido com sucesso")
        else:
            print("Fornecedor não encontrado")
    
    def mostrarFornecedor(self):
        x = DaoFornecedor().read()
        if x:
            for i in x:
                print(f"Nome: {i.nome} | Telefone: {i.telefone} | CNPJ: {i.cnpj} | Categoria: {i.categoria}")
        else:
            print("Nenhum fornecedor cadastrado")

class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa().read()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        listaEmail = list(filter(lambda x: x.email == email, x))
        listaEndereco = list(filter(lambda x: x.endereco == endereco, x))

        if len(listaCpf) > 0 or len(listaTelefone) > 0 or len(listaEmail) > 0 or len(listaEndereco) > 0:
            print("Cliente já cadastrado")
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                cliente = Pessoa(nome, telefone, cpf, email, endereco)
                DaoPessoa.save(cliente)
                print("Cliente cadastrado com sucesso")
            else:
                print("Digite dados validos, verifique o CPF ou o Telefone")

    def editarCliente(self, nomeAntigo, nomeNovo, telefoneNovo, cpfNovo, emailNovo, enderecoNovo):
        x = DaoPessoa().read()
        listaNome = list(filter(lambda x: x.nome == nomeAntigo, x))
        listaCpf = list(filter(lambda x: x.cpf == cpfNovo, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefoneNovo, x))
        listaEmail = list(filter(lambda x: x.email == emailNovo, x))
        listaEndereco = list(filter(lambda x: x.endereco == enderecoNovo, x))

        if len(listaNome) > 0:
            if len(listaCpf) == 0 and len(listaTelefone) == 0 and len(listaEmail) == 0 and len(listaEndereco) == 0:
                if len(cpfNovo) == 11 and len(telefoneNovo) <= 11 and len(telefoneNovo) >= 10:
                    cliente = Pessoa(nomeNovo, telefoneNovo, cpfNovo, emailNovo, enderecoNovo)
                    x = list(filter(lambda x: x.nome != nomeAntigo, x))
                    with open('clientes.txt', 'w') as arq:
                        for i in x:
                            arq.write(i.nome + " | " + i.telefone + " | " + i.cpf + " | " + i.email + " | " + i.endereco + "\n")
                    DaoPessoa.save(cliente)
                    print("Cliente editado com sucesso")
                else:
                    print("Digite dados validos, verifique o CPF ou o Telefone")
            else:
                print("Cliente já cadastrado")
        else:
            print("Cliente não encontrado")
    
    def removerCliente(self, nome):
        x = DaoPessoa().read()
        listaNome = list(filter(lambda x: x.nome == nome, x))
        if len(listaNome) > 0:
            x = list(filter(lambda x: x.nome != nome, x))
            with open('clientes.txt', 'w') as arq:
                for i in x:
                    arq.write(i.nome + " | " + i.telefone + " | " + i.cpf + " | " + i.email + " | " + i.endereco + "\n")
            print("Cliente removido com sucesso")
        else:
            print("Cliente não encontrado")
    
    def mostrarCliente(self):
        x = DaoPessoa().read()
        if x:
            for i in x:
                print(f"Nome: {i.nome} | Telefone: {i.telefone} | CPF: {i.cpf} | Email: {i.email} | Endereço: {i.endereco}")
        else:
            print("Nenhum cliente cadastrado")