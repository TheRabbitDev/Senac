#Atividade de Python - Exercicio 4: Valor do ingresso - Jhuan Araújo de Souza - 3ºA (T1)

print("\nSeja bem vindo ao terminal!\nPreço das passgens:\n \nPara viagens de até 200km - R$1,00 por Km\nPara viagens acima de 200km - R$0,50 por Km\n")
distancia = float(input("\nFavor insira a distancia que pretende percorrer: "))
valor_ingresso_200 = distancia * 1.0
valor_ingresso_201 = distancia * 0.5

if(distancia <= 200.0):
    print("O valor de seu ticket ficou em:", valor_ingresso_200)
else:
    print("O valor de seu ticket ficou em:", valor_ingresso_201)