if __name__ == "__main__":
    minha_conta = carregar_dados() # Chamar carregar_dados() para obter uma instância de ContaBancaria.add()

    # Exemplo de como você poderia ter uma segunda conta (para transferência)
    outra_conta = carregar_dados(filename="banco_secundario.json")
    if outra_conta._numero_conta == "00000-0": # Se for uma conta recém-criada (não caregada de arquivo)
        outra_conta._numero_conta + "54321-Y" # Atribui um número real para demonstração

    while True: # Manter o loop while TRue que exibe o menu de opções.    
        print("\n--- Olá! Bem-vindo ao seu banco virtual. ---")
        print("---------------------------------------")
        print("1 - Consultar Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Exibir Extrato")
        print("5 - Transferir")
        print("6 - Sair")
        print("----------------------------------------")

        opcao_str = input("Digite a opção desejada: ")
        try:
            opcao = int(opcao_str)
            if not (1 <= opcao <= 6): # Validar a opção escolhida
                print("Opção inválida. Por favor, digite um número entre 1 e 6.")
                continue # Continua o loop para pedir a opção novamente
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro. ")
            continue

        if opcao == 1:
            minha_conta.consultar_saldo()
        elif opcao == 2:
            valor = input("Digite o valor a depositar: R$ ")
            minha_conta.depositar(valor)
        elif opcao == 3:
            valor = input("Digite o valor a sacar: R$ ")
            minha_conta.sacar(valor)
        elif opcao == 4:
            minha_conta.exibir_extrato()
        elif opcao == 5:
            print(f"\nRealizando tranferência da conta '{minha_conta.numero_conta}' para '{outra_conta._numero_conta}'")
            valor_tranferencia = input("Digite o valor a ser transferido: R$ ")
            minha_conta.tranferir(outra_conta, valor_tranferencia)
        elif opcao == 6:
            salvar_dados(minha_conta) # Salvar os dados da conta principal antes de sair. 
            salvar_dados(outra_conta, filename="banco_secundario.json") # Salvar a segunda conta também
            print("Obrigado por utilizar nosso banco virtual!")
            break                         