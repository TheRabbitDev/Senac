#Lista de exercicios de Funçoes Python - Exercicio 1 - Jhuan Araújo de Souza - T1 3ºA

#Apresenteção do exercicio:

print("\nEsse programa faz a soma de valores, por favor insira os a seguir:")

#Definição de modulo:

def modulo_soma(valor_1, valor_2, valor_3, valor_4):
    return valor_1 + valor_2 + valor_3 + valor_4

#Insersão manual de dados:

valor_1 = float(input("\nDigite o primeiro valor:"))
valor_2 = float(input("Digite o segundo valor:"))
valor_3 = float(input("Digite o terceiro valor:"))
valor_4 = float(input("Digite o quarto valor:"))

#Finalização do programa:

print(f"O valor da soma é igual a: {modulo_soma(valor_1, valor_2, valor_3, valor_4)}")
