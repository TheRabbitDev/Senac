from datetime import datetime
from os import times
from time import time

class Cliente:
    def __init__(self, nome, sobrenome, idade, data_nascimento, cpf, rg, cidade, estado, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, titular, limite, saldo):
        self.agencia = agencia
        self.limite = limite
        self.saldo = saldo
        self.titular = titular
        self.historico = []

    def sacar(self, valor):
        now = datetime.now()
        if(self.saldo >= valor):
            self.saldo -= valor
            self.historico.append(f"{now.day}/{now.month}/{now.year} - " "Saque de {}".format(valor))
        else:
            print("\nOps ocorreu um erro:\nO valor selecionado é invalido, favor tente novamente")

    def depositar(self,valor):
        now = datetime.now()
        self.saldo += valor
        self.historico.append(f"{now.day}/{now.month}/{now.year} - " "Deposito de {}".format(valor))
        

    def emitir_extrato(self):
        now = datetime.now()
        print("\n[__________.__________.|E X T R A T O|.__________.___________]")
        print(f"Extrato atualizado em: {now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}")
        print(f"Agencia: {self.agencia}\nTitular: {self.titular.nome}\nSaldo: {self.saldo}\nLimite: {self.limite}")

    def emitir_historico(self):
        for x in self.historico:
            print(x)



        