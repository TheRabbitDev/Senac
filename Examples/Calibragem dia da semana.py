#Atividade de Python - Exercicio 2: Calibragem dia da semana - Jhuan Araújo de Souza - 3ºA (T1)

print("\nLista de dias da semana:\n1- Domingo\n2 - Segunda-feira\n3 - Terça feira\n4 - Quarta-feira\n5 - Quinta-feira\n6 - Sexta-feira\n7 - Sábado")
dia_da_semana = int(input("Favor selecione o dia em que estamos para a calibragem do sistema: "))

while (dia_da_semana > 7 or dia_da_semana < 1):
    print("Erro\nO número inserido não esta presente nos dados informados\nPor favor insira um número válido")
    dia_da_semana = int(input("Favor selecione o dia em que estamos para a calibragem do sistema: "))

if(dia_da_semana == 1):

    print("Sistema calibrado! Hoje é Domingo")

elif(dia_da_semana == 2):

    print("Sistema calibrado! Hoje é Segunda-feira")
    
elif(dia_da_semana == 3):

    print("Sistema calibrado! Hoje é Terça-feira")

elif(dia_da_semana == 4):

    print("Sistema calibrado! Hoje é Quarta-feira")

elif(dia_da_semana == 5):

    print("Sistema calibrado! Hoje é Quinta-feira")

elif(dia_da_semana == 6):

    print("Sistema calibrado! Hoje é Sexta-feira")

elif(dia_da_semana == 7):

    print("Sistema calibrado! Hoje é Sábado")

