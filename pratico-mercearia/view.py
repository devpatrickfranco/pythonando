import controller
import os

def criarArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.writelines("")

criarArquivos("categorias.txt", "estoque.txt", "vendas.txt", "clientes.txt", "fornecedores.txt")

# ──────────────────────────────────────────────
#  Submenus
# ──────────────────────────────────────────────

def menuCategoria():
    cat = controller.ControllerCategoria()
    while True:
        opcao = int(input("""
        ── CATEGORIAS ──
        1 - Cadastrar categoria
        2 - Remover categoria
        3 - Alterar categoria
        4 - Mostrar categorias
        0 - Voltar
        >> """))

        if opcao == 1:
            nome = input("Nome da categoria: ")
            cat.cadastrarCategoria(nome)

        elif opcao == 2:
            nome = input("Nome da categoria a remover: ")
            cat.removerCategoria(nome)

        elif opcao == 3:
            nome = input("Nome da categoria atual: ")
            novo = input("Novo nome da categoria: ")
            cat.alterarCategoria(nome, novo)

        elif opcao == 4:
            cat.mostrarCategorias()

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


def menuEstoque():
    est = controller.ControllerEstoque()
    while True:
        opcao = int(input("""
        ── ESTOQUE ──
        1 - Cadastrar produto
        2 - Remover produto
        3 - Alterar produto
        4 - Mostrar estoque
        0 - Voltar
        >> """))

        if opcao == 1:
            nome      = input("Nome do produto: ")
            preco     = input("Preço: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade: "))
            est.cadastrarProduto(nome, preco, categoria, quantidade)

        elif opcao == 2:
            nome = input("Nome do produto a remover: ")
            est.removerProduto(nome)

        elif opcao == 3:
            nome      = input("Nome do produto atual: ")
            novoNome  = input("Novo nome: ")
            novoPreco = input("Novo preço: ")
            novaQtd   = int(input("Nova quantidade: "))
            novaCat   = input("Nova categoria: ")
            est.alterarProduto(nome, novoNome, novoPreco, novaQtd, novaCat)

        elif opcao == 4:
            est.mostrarEstoque()

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


def menuVendas():
    vnd = controller.ControllerVenda()
    while True:
        opcao = int(input("""
        ── VENDAS ──
        1 - Registrar venda
        2 - Mostrar vendas por período
        3 - Relatório de produtos mais vendidos
        0 - Voltar
        >> """))

        if opcao == 1:
            produto    = input("Nome do produto: ")
            vendedor   = input("Vendedor: ")
            comprador  = input("Comprador: ")
            quantidade = int(input("Quantidade: "))
            vnd.cadastrarVenda(produto, vendedor, comprador, quantidade)

        elif opcao == 2:
            dataInicio = input("Data início (dd/mm/aaaa): ")
            dataFim    = input("Data fim   (dd/mm/aaaa): ")
            vnd.mostrarVenda(dataInicio, dataFim)

        elif opcao == 3:
            vnd.relatorioVendas()

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


def menuClientes():
    cli = controller.ControllerCliente()
    while True:
        opcao = int(input("""
        ── CLIENTES ──
        1 - Cadastrar cliente
        2 - Editar cliente
        3 - Remover cliente
        4 - Mostrar clientes
        0 - Voltar
        >> """))

        if opcao == 1:
            nome      = input("Nome: ")
            telefone  = input("Telefone (10-11 dígitos, sem espaços): ")
            cpf       = input("CPF (11 dígitos, sem pontos): ")
            email     = input("E-mail: ")
            endereco  = input("Endereço: ")
            cli.cadastrarCliente(nome, telefone, cpf, email, endereco)

        elif opcao == 2:
            nomeAntigo   = input("Nome atual do cliente: ")
            nomeNovo     = input("Novo nome: ")
            telefoneNovo = input("Novo telefone: ")
            cpfNovo      = input("Novo CPF: ")
            emailNovo    = input("Novo e-mail: ")
            enderecoNovo = input("Novo endereço: ")
            cli.editarCliente(nomeAntigo, nomeNovo, telefoneNovo, cpfNovo, emailNovo, enderecoNovo)

        elif opcao == 3:
            nome = input("Nome do cliente a remover: ")
            cli.removerCliente(nome)

        elif opcao == 4:
            cli.mostrarCliente()

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


def menuFornecedores():
    forn = controller.ControllerFornecer()
    while True:
        opcao = int(input("""
        ── FORNECEDORES ──
        1 - Cadastrar fornecedor
        2 - Editar fornecedor
        3 - Remover fornecedor
        4 - Mostrar fornecedores
        0 - Voltar
        >> """))

        if opcao == 1:
            nome      = input("Nome: ")
            cnpj      = input("CNPJ (14 dígitos, sem pontos): ")
            telefone  = input("Telefone (10-11 dígitos, sem espaços): ")
            categoria = input("Categoria: ")
            forn.cadastrarFornecedor(nome, cnpj, telefone, categoria)

        elif opcao == 2:
            nomeAntigo   = input("Nome atual do fornecedor: ")
            nomeNovo     = input("Novo nome: ")
            cnpjNovo     = input("Novo CNPJ: ")
            telefoneNovo = input("Novo telefone: ")
            categoriaNova = input("Nova categoria: ")
            forn.editarFornecedor(nomeAntigo, nomeNovo, cnpjNovo, telefoneNovo, categoriaNova)

        elif opcao == 3:
            nome = input("Nome do fornecedor a remover: ")
            forn.removerFornecedor(nome)

        elif opcao == 4:
            forn.mostrarFornecedor()

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


# ──────────────────────────────────────────────
#  Menu principal
# ──────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        local = int(input("""
        ══════════════════════════
              MERCEARIA
        ══════════════════════════
        1 - Categorias
        2 - Estoque
        3 - Vendas
        4 - Clientes
        5 - Fornecedores
        6 - Sair
        >> """))

        os.system('clear')
        if local == 1:
            menuCategoria()
        elif local == 2:
            menuEstoque()
        elif local == 3:
            menuVendas()
        elif local == 4:
            menuClientes()
        elif local == 5:
            menuFornecedores()
        elif local == 6:
            os.system('clear')
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida!")