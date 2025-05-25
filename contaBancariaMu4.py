def salvar_dados(conta, filename="banco_dados.json"):
    """ Salva o saldo e o extrato de uma conta em um arquivo JSON."""
    dados = {
        "numero_conta": conta._numero_conta, # Incluir o número da conta para recriar o objeto
        "saldo": conta.saldo,
        "extrato": conta.extrato
    }

    with open(filename, "w") as f: # Abre o arquivo "banco_dados.json" em modo de escrita ("w")
        # Salva o saldo e o extrato no arquivo usando json.dump()
        json.dump(dados, f, indent=4) # O 'indent-4' é para formatar o JSON de forma legível
    print(f"Dados da conta '{conta._numero_conta}' salvos com sucesso!")

def carregar_dados(filename="banco_dados.json"):
    """Carrega o saldo e o extrato de uma conta a partir de um arquivo JSON."""
    try: # Tentar abrir um arquivo chamado "banco_dados.json" em modo de leitura ("r"). 
       with open(filename, "r") as f:
           dados = json.load(f) # Se o arquivo existir, carregar o saldo e o extrato de lá. 
           # Retorna uma nova instância de ContaBancaria com os dados carregados
           return ContaBancaria(dados["numero_conta"], dados["saldo"], dados["extrato"])
    except FileNotFoundError: #Se o arquivo não existir (FileNotFoundError), definir o saldo inicial e o extrato como uma lista vazia. 
        print("Arquivo de dados não encontrado. Criando nova conta com número padrão '00000-0'.")
        return ContaBancaria(00000-0) # Retorna uma nova conta com um número padrão se o arquivo não for encontrado           
