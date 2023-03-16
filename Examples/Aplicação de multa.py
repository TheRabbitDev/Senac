#Atividade de Python - Exercicio 3: Aplicação de multa - Jhuan Araújo de Souza - 3ºA (T1)

velocidade_do_carro = int(input("\nFavor insira a velocidade do carro: "))
velocidade_limite = 50
multa = (velocidade_do_carro - velocidade_limite) * 200

if(velocidade_do_carro < 50):
    print("A velocidade do carro não excede o limite máximo da via")
else:
    print("O veiculo foi multado, a velocidade capturada foi de", velocidade_do_carro, "Km/h.\nSua multa foi de R$", multa)