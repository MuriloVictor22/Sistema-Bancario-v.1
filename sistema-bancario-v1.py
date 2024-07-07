import os

menu = """
	[D] Depositar
	[S] Sacar
	[E] Extrato
	[Q] Sair.

 -> """

saldo = 0
limite = 500
extrato = "============= EXTRATO ============"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).upper()
    
    match opcao:
        case "D":
            deposito = int(input("Depositar: "))
            if deposito >= 0:
                saldo += deposito
                extrato += f"\nDepósito: R$ {deposito:.2f}."
                os.system("cls")
                print("Depósito realizado com sucesso!")
            else:
                os.system("cls")
                print("Apenas números positivos.")
            
        case "S":
            sacar = int(input("Sacar: "))
            if sacar > limite:
                os.system("cls")
                print("Apenas saques de R$500.00 ou menores que R$ 500.00.")
            elif saldo < sacar:
                os.system("cls")
                print("Você não possue saldo suficiente.")
            elif numero_saques == LIMITE_SAQUES:
                os.system("cls")
                print("Você já excedeu o número de saques diários.")
            else:
                saldo -= sacar
                extrato += f"\nSaque: R$ {sacar:.2f}."
                numero_saques += 1
                os.system("cls")
                print("Saque realizado com sucesso!")
        case "E":
            print(extrato)
            print(f"\nSALDO ATUAL: R$ {saldo:.2f}.")
            print("==================================")
        case "Q":
            break
        
        case _:
            os.system("cls")
            print("Operação Inválida! Atente-se as opções:")
            

