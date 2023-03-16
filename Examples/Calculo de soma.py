# Atividade de Python - Exercicio 7: Calculo de soma - Jhuan Araújo de Souza - 3ºA (T1)

#Criação da função somar

def somar(valor_x, valor_y, valor_z):
    resultado = valor_x + valor_y+ valor_z 
    print("A soma dos numeros é", resultado)

#Criação da função de valores

def menu_valores():

#Declaração de variaveis

    valor_x = float(input("Digite um valor qualquer para X: "))
    valor_y = float(input("Digite um valor qualquer para Y: "))
    valor_z = float(input("Digite um valor qualquer para Z: "))

    somar(valor_x, valor_y, valor_z)

#Resultado final

menu_valores()
    

