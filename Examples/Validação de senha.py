#Atividade de Python - Exercicio 1: Validação de senha - Jhuan Araújo de Souza - 3ºA (T1)

login = 1

nome_de_usuario = input("\nPor favor, digite seu nome de usuario: ") 

while(login):

    senha = input("Insira sua senha por favor: ")

    if (senha == nome_de_usuario):

        print("ops, ocorreu um erro!\nA sua senha não pode ser igual ao seu nome de usuário\nFavor, tente novamente")

        continue

    else:
        
        login = 0
        print("Seja bem vindo", nome_de_usuario)