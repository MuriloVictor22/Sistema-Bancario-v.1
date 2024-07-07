import os
import textwrap

menu = """
============= MENU ============
[NU]\tNovo Usuario
[NC]\tNova Conta
[D]\tDepositar
[S]\tSacar
[E]\tExtrato
[Q]\tSair.

 -> """

saldo = 0
limite = 500
extrato = "============= EXTRATO ============"
numero_saques = 0
usuarios = []
contas = []

LIMITE_SAQUES = 3
AGENCIA = "0001"


def depositar(saldo, valor, extrato, /):
    if valor >= 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}."
        os.system("cls")
        print("Depósito realizado com sucesso!")
    else:
        os.system("cls")
        print("Apenas números positivos.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques:
        os.system("cls")
        print("Você já excedeu o número de saques diários.")
    elif valor > limite:
        os.system("cls")
        print("Apenas saques de R$500.00 ou menores que R$ 500.00.")
    elif saldo < valor:
        os.system("cls")
        print("Você não possue saldo suficiente.")
    else:
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}."
        numero_saques += 1
        os.system("cls")
        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, *, extrato):
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def criar_usuario(usuarios):
    cpf = input("CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        os.system("cls")
        print("Já existe um usuário com esse CPF.")
        return
    
    nome = input("NOME COMPLETO: ")
    data_nascimento = input("DATA DE NASCIMENTO (dd/mm/aaaa): ")
    endereco = input("ENDEREÇO: ")
            
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })
    
    os.system("cls")
    print("Usuário cadastrado com sucesso!")
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
        
    if usuario:
        os.system("cls")
        print("Nova conta criada com sucesso!")
        
        return {
			"agencia": agencia,
			"numero_conta": numero_conta,
			"usuario": usuario
		}
    
    os.system("cls")
    print("Usuário não encontrado. Você pode criar um usuário na opção [NU].")

while True:
    opcao = input(menu).upper()

    match opcao:
        case "NU":
            criar_usuario(usuarios)
        
        case "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        case "D":
            valor = int(input("Depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            exibir_extrato(saldo, extrato=extrato)

        case "S":
            valor = int(input("Sacar: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            exibir_extrato(saldo, extrato=extrato)

        case "E":
            print(extrato)
            print(f"\nSALDO ATUAL: R$ {saldo:.2f}.")
            print("==================================")

        case "Q":
            break

        case _:
            os.system("cls")
            print("Operação Inválida! Atente-se as opções:")
