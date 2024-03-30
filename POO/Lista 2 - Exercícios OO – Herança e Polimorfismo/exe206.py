'''6) Sistema de Contas Bancárias
Crie um programa para um sistema de contas bancárias que gerencia diferentes
tipos de contas, como contas correntes e contas de poupança. Cada tipo de conta tem
suas próprias regras para depósitos, saques e cálculos de juros. Crie classes pararepresentar os diferentes tipos de contas e
implemente métodos para realizar operações bancárias.

Crie uma classe abstrata chamada ContaBancaria com campos para número da conta, saldo e titular.

Inclua métodos abstratos para depositar(), sacar(), e calcularJuros().

Crie duas classes que herdam de ContaBancaria: ContaCorrente e ContaPoupanca.

Na classe ContaCorrente, o método depositar() permite depósitos ilimitados, mas cobra uma taxa de manutenção mensal.
O método sacar() permite saques, mas pode verificar se há fundos suficientes.
A taxa de manutenção mensal é descontada automaticamente do saldo.

Na classe ContaPoupanca, o método depositar() permite depósitos ilimitados e o método sacar() permite saques,
desde que haja saldo suficiente.
O método calcularJuros() calcula e adiciona juros mensais à conta com base em uma taxa de juros fixa.'''

class ContaBancaria:
    def __init__(self):
        self.numero_da_conta = 0
        self.saldo = 0
        self.titular = " "

    def set_numero_da_conta(self, numero_da_conta):
        self.numero_da_conta = numero_da_conta

    def get_numero_da_conta(self):
        return self.numero_da_conta

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def depositar(self):
       pass

    def sacar(self, valor):
        if valor > self.saldo:
            return "saldo insuficiente"
        else:
            self.set_saldo(self.get_saldo() - valor)
            return "saque efetivado"

class ContaCorrente(ContaBancaria):
    def __init__(self):
        ContaBancaria.__init__(self)
        self.taxa = 0

    def set_taxa(self, taxa):
        self.taxa = taxa

    def get_taxa(self):
        return self.taxa

    def depositar(self, valor):
        return self.set_saldo(self.get_saldo() + valor - self.get_taxa())

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        ContaBancaria.__init__(self)
        self.taxa_juros_fixa = 0

    def set_taxa_juros_fixa(self,taxa_juros_fixa):
        self.taxa_juros_fixa = taxa_juros_fixa

    def get_taxa_juros_fixa(self):
        return self.taxa_juros_fixa


    def depositar(self, valor):
        return self.set_saldo(self.get_saldo() + valor)


    def calcularJuros(self, taxa):
        juros = self.get_saldo() * taxa / 100
        return self.set_saldo( self.get_saldo() + juros)


contaCorrente = ContaCorrente()
contaCorrente.set_saldo(1000)
print(contaCorrente.sacar(900))
print(f"Saldo = {contaCorrente.get_saldo():.2f}")
contaCorrente.set_taxa(100)
contaCorrente.depositar(50)
print(f"Saldo = {contaCorrente.get_saldo():.2f}")

print(" ")

contaPoupanca = ContaPoupanca()
contaPoupanca.set_saldo(1000)
contaPoupanca.depositar(100)
print(contaPoupanca.sacar(900))
contaPoupanca.calcularJuros(1)
print(f"Saldo = {contaPoupanca.get_saldo():.2f}")





