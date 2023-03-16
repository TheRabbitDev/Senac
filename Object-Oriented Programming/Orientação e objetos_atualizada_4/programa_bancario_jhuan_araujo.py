# Importação de classes

from classes import Conta, Cliente


# Inicio do programa

print("\n\n[__________.__________.|  B A N C O  |.__________.___________]")

condicao = True

print("\nSeja bem vindo ao aplicativo do seu banco digital\nPor favor faça login ou cadastre-se")

# Seleção  de loguin ou cadastro (Menu 1)

while(condicao):
    selecao_menu_1 = float(
        input("\n[  1 - Login  | 2 - Cadastro ]\nDigite o numero: "))

# Login

    if (selecao_menu_1 == 1):
        print("\nOps ocorreu um erro:\nEsta parte da aplicação ainda não foi programada, por favor selecione outro numero\n")
        condicao = True

# Cadastro

    elif (selecao_menu_1 == 2):
        print("\n[_______________________________________________________]")

        cadastro_usuario = Cliente(nome=input("\nFavor preeencha as informaçoes\nPrimeiro nome: "), sobrenome=input("Sobrenome: "), idade=float(input("Idade: ")), data_nascimento=input(
            "Data de nascimento: "), cpf=input("Cadastro de Pessoas Físicas (CPF): "), rg=input("Registro Geral (RG): "), cidade=input("Cidade onde mora: "), estado=input("Estado: "), endereco=input("Endereço: "))
        condicao_2 = True

# Verificção de idade

        while(condicao_2):

            # Maior de idade

            if(cadastro_usuario.idade >= 18):
                condicao_2 = False

# Menor de idade

            else:
                print(
                    "\nOps ocorreu um erro:\nDesculpe, os serviços do aplicativo são destinados apenas para maiores de idade")
                print(
                    "\nEncerrando sessão.\nEncerrando sessão..\nEncerrando sessão...\n")
                exit()

# Conta criada

        print("\n[__________.__________.__________.__________.___________]")
        print("\nCadastro concluido com sucesso! Sua conta foi criada.\nPor padrão o banco ajusta seu limite para R$800\nmas não se preocupe, voce pode ajustar isso depois")

# Inserção

        conta_cliente = Conta(f"0001", cadastro_usuario, 800, saldo=float(
            input("\nInsira o valor do seu saldo inicial por favor: ")))
        print("\nProcessando.\nProcessando..\nProcessando...\nProcessando.\nProcessando..\nProcessando...\n\nSegue abaixo as informações da sua conta do banco:")
        print(f"\nAgencia: {conta_cliente.agencia}\nTitular: {cadastro_usuario.nome}\nLimite: {conta_cliente.limite}\nSaldo: {conta_cliente.saldo}")

        condicao = False

# Mensagem de erro caso selecionar um numero inexistente no menu 1

    else:
        print(
            "\nOps ocorreu um erro:\nO numero selecionado é invalido, favor tente novamente")
        condicao = True

# Seleção das funçoes do Menu 2

condicao_1 = True

while(condicao_1):
    print("\n[__________.__________.|   M E N U   |.__________.___________]")
    print("\nSelecione uma opção")
    selecao_menu_2 = float(input(
        "\n[  1 - Sacar  | 2 - Depositar | 3 - Emitir Extrato | 4 - Emitir Histórico | 5 - Encerrar Sessão ]\nDigite o numero: "))

#Seleção: Sacar

    if (selecao_menu_2 == 1):
        print("\n[__________.__________.|   S A C A R   |.__________.___________]")
        valor = float(input("\nPor favor selecione um valor a sacar: "))
        Conta.sacar(conta_cliente, valor)
        Conta.emitir_extrato(conta_cliente)
        print("\nRetornando ao menu.\nRetornando ao menu..\nRetornando ao menu...\n\n\n")

#Seleção: Depositar

    elif(selecao_menu_2 == 2):
        print(
            "\n[__________.__________.|   D E P O S I T A R   |.__________.___________]")
        valor = float(input("\nPor favor selecione um valor a depositar: "))
        Conta.depositar(conta_cliente, valor)
        Conta.emitir_extrato(conta_cliente)
        print("\nRetornando ao menu.\nRetornando ao menu..\nRetornando ao menu...\n\n\n")

# Seleção: Emitir Extrato

    elif(selecao_menu_2 == 3):
        print(
            "\n[__________.__________.|   E X T R A T O   |.__________.___________]")
        Conta.emitir_extrato(conta_cliente)
        print("\nRetornando ao menu.\nRetornando ao menu..\nRetornando ao menu...\n\n\n")

# Seleção: Emitir Histórico

    elif(selecao_menu_2 == 4):
        print(
            "\n[__________.__________.|   H I S T O R I C O   |.__________.___________]")
        Conta.emitir_historico(conta_cliente)

# Seleção: Sair da aplicação

    elif(selecao_menu_2 == 5):

        condicao_sair = True
        while(condicao_sair):
            sair = float(
                input("\n[  1 -  Sim   | 2 -  Não  ]\nDigite o numero: "))

# Sim sair

            if(sair == 1):
                print(
                    "\nSim selecionado\nEncerrando sessão.\nEncerrando sessão..\nEncerrando sessão...\n")
                exit()

# Não sair

            elif(sair == 2):
                print(
                    "\nNão selecionado\nVoltando a aplicação.\nVoltando a aplicação..\nVoltando a aplicação...")
                condicao_sair = False

# Erro de seleção

            else:
                print(
                    "\nOps ocorreu um erro:\nO número selecionado é invalido, favor tente novamente")
                condicao_sair = True

# Erro de seleção

    else:
        print(
            "\nOps ocorreu um erro:\nO numero selecionado é invalido, favor tente novamente")
        condicao_1 = True
