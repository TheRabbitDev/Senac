#Atividade de Python - Exercicio 5: Conta de luz - Jhuan Araújo de Souza - 3ºA (T1)

#Introdução

print("[============================================== (Consultoria Wesley F.) ==============================================]")
print("Seja bem vindo a consultoria de contas de luz!")
print("\nTabela de preços por tipo e faixa de consumo:")
print("\nR - Residencial\n•Consumo de até 500kWh - R$0,45\n•Consumo acima de 500kWh - R$0,65")
print("\nC - Comercial\n•Consumo de até 1000kWh - R$0,55\n•Consumo acima de 1000kWh - R$0,60")
print("\nI - Industrial\n•Consumo de até 5000kWh - R$0,55\n•Consumo acima de 5000kWh - R$0,60")

#declaração de variaveis

tipo = input("\nFavor insira o tipo de consumo (R, C ou I): ")
quantidade = float(input("Favor insira a quatidade de kWh consumido: "))

R = "R"
C = "C"
I = "I"

#Calculos

conta_R1 = quantidade * 0.45
conta_R2 = quantidade * 0.65
conta_C1 = quantidade * 0.55
conta_C2 = quantidade * 0.60
conta_I1 = quantidade * 0.55
conta_I2 = quantidade * 0.60

#Mensagem de erro caso o tipo não seja selecionado corretamente

Erro = 1

while(Erro):

    excessao = (tipo != R and tipo != C and tipo != I)

    if(excessao):
        print("\nOps, ocorreu um erro\nO tipo de consumo inserido não condiz com os dados informados\nFavor inserir um dado valido")
        tipo = input("\nFavor insira o tipo de consumo (R, C ou I): ")

    else:
        Erro = 0

#Resultados 

if(tipo == R):
    if(quantidade <= 500):
        print("\nSeu tipo escolhido foi", tipo, "\nBaseado no seu consumo, sua conta sera de:", conta_R1, "reais")
    else:
        print("\nSeu tipo escolhido foi", tipo, "\nBaseado no seu consumo, sua conta sera de:", conta_R2, "reais")
elif(tipo == C):
    if(quantidade <= 1000):
        print("\nSeu tipo escolhido foi", tipo, "\nBaseado no seu consumo, sua conta sera de:", conta_C1, "reais")
    else:
        print("\nSeu tipo escolhido foi", tipo, "\nBaseado no seu consumo, sua conta sera de:", conta_C2, "reais")
elif(tipo == I):
    if(quantidade <= 5000):
        print("\nSeu tipo escolhido foi", tipo, "\nBaseado no seu consumo, sua conta sera de:", conta_I1, "reais")
    else:
        print("\nSeu tipo escolhido foi", tipo, "\nBaseado no seu consumo, sua conta sera de:", conta_I2, "reais")

print("[============================================== (         Fim          ) ==============================================]") 