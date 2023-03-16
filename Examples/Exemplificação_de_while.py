#Atividade de Python - Exercicio 8: Exemplificação de while - Jhuan Araújo de Souza - 3ºA (T1)

#A estrutura while realiza uma repetição enquanto algum valor definido for verdadeiro, apenas parando de repetir caso esse valor definnido se torne falso

print("\nA resolução para a conta 1140 + 330 é igual a:")

print("\nA - 1500\nB - 1470\nC - 1400\nD - 1460\nE - 1480")

resposta = input("\nFavor isira a letra correta: ")

#Por exemplo aqui eum criei uma variavel de valor verdadeiro, e coloquei ela como parametro de analise no while
#Ou seja o while só parara de repetir para insrir o numero correto nopvamente se essa variavel se tornar falsa

letra_errada = 1

while (letra_errada):
    if(resposta != "B"):
        print("Desculpe você errou a letra, sua letra selecionada foi:", resposta, "favor tente novamente.")
        resposta = input("\nFavor isira a letra correta: ")
    else:
        print("Parabens! sua resposta esta correta, a letra selecionada foi: ", resposta)
        letra_errada = 0

#A variavel apenas se torna falsa quando a resposta correta for atingida