saldo = 0
extrato = []
LIMITE_SAQUES = 0

while True:
    opcao = input('''
        Digite [1] se deseja depositar
        Digite [2] se deseja sacar 
        Digite [3] se deseja ver seu extrato bancário
        Digite [Q] se deseja sair do sistema 
        ''')

    if opcao == "1":
        deposito = float(input("Digite qual valor deseja depositar: "))
        if deposito < 0:
            print("[Erro] deposite um valor válido")
        else:
            saldo += deposito
            extrato.append(("depósito", deposito))

    elif opcao == "2":
        print("Saldo atual:", saldo)
        saque = float(input("Digite quanto você deseja sacar: "))
        if LIMITE_SAQUES >= 3:
            print("Você atingiu o limite diário de 3 saques por dia.")
            continue
        if saque > saldo:
            print("[Erro] não há saldo suficiente")
        elif saque < 0:
            print("[Erro] Saque um valor válido")
        elif saque > 500:
            print("Só são permitidos saques até o valor de R$ 500")
        else:
            saldo -= saque
            extrato.append(("saque", saque))
            LIMITE_SAQUES += 1
                
    elif opcao == "3":
        print("==========Aqui está seu extrato:===========")
        print(f'Saldo: {saldo: .2f}')
        for transacao in extrato:
            tipo, valor = transacao
            print(f"{tipo.title()}: R$ {valor}")
        print("==========================================")

    elif opcao.upper() == "Q":
        break

    else:
        print("[Erro] Digite uma opção válida.")
        continue
