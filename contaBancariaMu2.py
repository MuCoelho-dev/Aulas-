import datetime
class ContaBancaria():
    """
    Representa uma conta bancária com saldo e histórico de transações.
    """
    #Método Construtor que defini os atributos dos objetos a serem criados(instanciados)
    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self.saldo = saldo_inicial
        self._numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []
    def consultar_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Seu saldo atual é: R$ {self.saldo:.2f}")
    def depositar(self, valor):
        try:
            valor_deposito = float(valor)
            if valor_deposito <= 0:
                print("Valor de depósito inválido. Digite um número positivo.")
                return
            self.saldo += valor_deposito
            
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%y %H:%M:%S"),
                "tipo": "Depósito",
                "valor": valor_deposito
            })         
            print(f"epósito de R$ {valor_deposito:.2f} realizado com sucesso.")
            print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
        except ValueError:
            print("Valor inválido para depósito. Por favor, difite um número.")
    def sacar(self, valor):
        
        try:
            valor_saque = float(valor)
            if valor_saque <= 0:
                print("Valor de saque inválido. Digite um número positivo.")
                return
            if valor_saque <= self.saldo:
                self.saldo -= valor_saque
                agora= datetime.datetime.now()
                self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo": "Saque",
                    "valor": valor_saque
                })
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
                print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Valor inválido para saque. Por favor, digite um número.")
            
if __name__ =="__main__":
    
    minha_conta = ContaBancaria(numero_conta="98765-4", saldo_inicial=50.0)
    print(f"Conta {minha_conta._numero_conta} criada com saldo: R$ {minha_conta.saldo:.2f}")
    
    print("\n=== Testando operações ---")
    minha_conta.consultar_saldo()
    
    minha_conta.depositar(200)
    minha_conta.consultar_saldo()
    
    minha_conta.sacar(150)
    minha_conta.consultar_saldo()
    
    minha_conta.sacar(700)
    minha_conta.consultar_saldo()
    
    minha_conta.depositar("abc")
    minha_conta.sacar("xyz")            
                        
           

