from controller import ControllerCadastro, ControllerLogin

while True:
    print("========== [MENU] ==========")
    decidir = int(input("Digite 1 para cadastrar\nDigite 2 para Logar\nDigite 3 para sair"))

    if decidir == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        resultado = ControllerCadastro.cadastrar(nome, email, senha)
         
        if resultado == 2:
            print("Tamanho do nome digitado invalido")
        elif resultado == 3:
            print("Email maior que 200 caracters")
        elif resultado == 4:
            print("Tamanho da senha invalida")
        elif resultado == 5:
            print("Email já cadastrado")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadsstro realizado com sucesso")

    elif decidir == 2:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
 
        resultado = ControllerLogin.login(email, senha)

        if not resultado:
            print('email ou senha invalidos')
        else:
            print('logado com sucesso!')
    else:
        break