
MENU = """

[1] DEPOSITO
[2] SAQUE
[3] EXTRATO
[4] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(MENU)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Falha na operação de Deposito, insira um valor valido ")
    
    elif opcao == "2":
        valor = float(input("informe o valor: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operacao falhou! Você execeu o limite.")
        
        elif excedeu_saques:
            print("operação falhou! Você execedeu o limite de saques")
        
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque =+ 1 
            
        else:
            print("Operacao falhou! O valor informado e invalido.")
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "4":
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")
