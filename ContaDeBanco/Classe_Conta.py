class Conta:
    # guarda as informações do usuario e realiza as funções e transações
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular.nome
        self.numero = numero
        self.saldo = saldo
        # lista para guardar as informações dos depositos  e saques
        self.saldo_depo = []
        self.saldo_saq = []

    def Extrato(self):
        # exibe o extrato do usuario com as suas informações e transações
        print(f'titular: {self.titular}'
              f'\nnumero: {self.numero}')
        print(60 * '\033[34m=\033[m')
        print(f'saldo: \033[32mR${self.saldo}\033[m')
        print(60 * '\033[34m=\033[m')
        for valor in self.saldo_depo:  # exibe todos os depositos
            print(f'deposito = R${valor}')
        for valor2 in self.saldo_saq:  # exibe todos os saques
            print(f'saque = R${valor2}')
        print(60 * '\033[34m=\033[m')

    def Deposito(self, deposito):
        # realiza um deposito na conta do usuário
        self.saldo += deposito
        print(f'Depositado: R${deposito}'
              f' Novo saldo: R${self.saldo}')
        # guarda a transação do usuario para o extrato
        self.saldo_depo.append(deposito)

    def Saque(self, saque):
        # realiza um saque na conta do usuário
        # verifica se o usuário tem dinheiro para sacar na conta
        if self.saldo < saque:
            print('\033[31mvoce não possui saldo o suficiente para realizar o saque\033[m')
        else:
            self.saldo -= saque
            print(f'Sacado: \033[31m- R${saque}\033[m'
                  f' Saldo Restante: \033[32mR${self.saldo}\033[m')
            # guarda a transação do usuário para o extrato
            self.saldo_saq.append(saque)
