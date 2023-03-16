#Lista de exercicios de Funçoes Python - Exercicio 3 - Jhuan Araújo de Souza - T1 3ºA

#Definição de modulo:

def modulo_conta(conta):
    gorjeta = (conta * 10) / 100
    return gorjeta

#Inserção manual de dados:

conta = float(input("Favor insira o valor total da conta: "))

total = conta + modulo_conta(conta)

#Finalização do programa:

print(f"Com uma conta no total de {conta}, o valor da gorjeta é: {modulo_conta(conta)}, potanto o valor final a se pagar é de: {total}")

