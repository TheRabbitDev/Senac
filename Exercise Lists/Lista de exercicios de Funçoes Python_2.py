#Lista de exercicios de Funçoes Python - Exercicio 2 - Jhuan Araújo de Souza - T1 3ºA

#Definição de modulo:

def modulo_sinal(numero):
    if(numero < 0):
        return print(f"{numero}, é negativo.")
    elif(numero > 0):
        return print(f"{numero}, é positivo.")
    else:
        return print(f"{numero}, possui valor e sinalização nulos.")

#Insersão manual de dados:

numero = float(input("Digite um numero, por favor:"))

#Finalização do programa:

print(f"O numero escolhido, {modulo_sinal(numero)}")
