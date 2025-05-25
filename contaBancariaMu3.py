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
    def exibir_extrato(self):
        """Exibe o histórico detalhado de transações da conta."""
    if not self.extrato:
        print("Não foram realizadas transações.")
    else:
        print("\n--- Extrato Bancário ---")
        for transacao in self.extrato:
            data_hora = transacao["data_hora"]
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")  
    def transferir(self, conta_destino, valor):
    
        try:
            
            valor_transferencia = float(valor)
            if valor_transferencia <= 0:
              print("Valor de transferêmcia inválido. Digite um número positivo.")
              return
            if not isinstance(conta_destino, ContaBancaria):
                     print("Erro: A conta de destino não é valida de ContaBancaria.")
                     return
            if valor_transferencia <= self.saldo:
                self.saldo -= valor_transferencia
                agora = datetime.datetime.now()
                self.extrato.append ({
                    "data_hora": agora.strftime("5d/%m/%Y 5H:%M:%$"),
                    "tipo": f"Transferêmcoa para {conta_destino._numero_conta}",
                    "valor": valor_transferencia
                })
                print(f"tranferência de R$ {valor_transferencia:.2f} para cont {conta_destino._numero_conta} realizada com sucesso.")
                print(f"Seu novo saldo é: R$ {sel.saldo:.2f}")
            
                conta_destino.depositar(valor_transferencia)
            else:
                print("Saldo insuficiente para realizar a transferência.")
        except ValueError:
            print("Valor inválido para transferência. Por favor, digite um número.") 
if __name__=="__main__":
    minha_conta = ContaBancaria(numero_conta="12345-x", saldo_inicial=1000.0)                                          
    conta_joao = ContaBancaria (numero_conta="67890-y", saldo_inicial=200.0)
    
    print(f"Conta {minha_conta._numero_conta} criada com saldo: R$ {minha_conta.saldo:.2f}")
    print(f"Conta {conta_joao._numero_conta} croada com saldo: R$ {conta_joao.saldo:.2f}")
    
    print("\n--- Realizando Operações para popular o extrato ---")
    minha_conta.depositar(300)
    minha_conta.sacar(150)
    
    print("\n-- Realizando Operações para popular o extrato ---")
    minha_conta.depositar(300)
    minha_conta.sacar(150)
    
    print("\n--- Testando Extrato (após operações) ---")
    
    print("\n-- Testando Transferência ---")
    minha_conta.transferir(conta_joao, 400)
    print("\n--- Saldos após transferência ---")
    minha_conta.consultar_saldo()
    conta_joao.consultar_saldo()
    
    print("\n--- Extrato da minha conta após transferência ---")
    minha_conta.exibir_extrato()
    
    print("\n--- Extrato da conta do joão após transferência ---")  
    conta_joao.exibir_extrato()
    
    minha_conta.tranferir(conta_joao, 1500)               
    