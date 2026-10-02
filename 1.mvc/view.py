from controller import PessoaController

while True:
    print("Digite 1 para cadastrar")
    print("Digite 2 para listar")
    print("Digite 3 para buscar uma pessoa")
    print("Digite 4 para sair")
    opcao = int(input("Digite sua opção: "))
    if opcao == 4:
        break
    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cpf = input("Digite o cpf: ")
        if PessoaController.cadastrar(nome, idade, cpf):
            print("Pessoa cadastrada com sucesso\n")
        else:
            print("Erro ao cadastrar pessoa, digite valores validos")
    if opcao == 2:
        PessoaController.allPeople()
        print("\n")
    if opcao == 3:
        cpf = input("Digite o cpf: ")
        PessoaController.onePerson(cpf)
            
