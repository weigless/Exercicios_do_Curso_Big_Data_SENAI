#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos,
# saques e consulte o saldo da conta, e sair

saldo=0
resposta= ""
print("===== CAIXA ELETRÔNICO =====")
while resposta!= 4:
    print("\n"
          "[1] Depósito\n"
          "[2] Saque\n"
          "[3] Consultar Saldo\n"
          "[4] Sair\n\n")
    resposta = int(input("Escolha uma opção: "))

    if resposta==1:
        valor=float(input("Digite o valor que deseja depositar: "))
        confirmacao=input(f"Confirma o depósito de R$ {valor:.2f} ? (S/N): ").upper().strip()
        if confirmacao== "N":
            print("------------------------------------------------")
            print("Operação cancelada.")
            print("------------------------------------------------")
        else:
            saldo+=valor
            print("------------------------------------------------")
            print(f"Depósito realizado no valor de R$ {valor:.2f}.")
            print("------------------------------------------------")
    elif resposta==2:
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor>saldo:
            print("------------------------------------------------")
            print("Não há saldo disponível.")
            print("------------------------------------------------")
        else:
            confirmacao = input(f"Confirma o saque de R$ {valor:.2f} ? (S/N): ").upper().strip()
            if confirmacao == "N":
                print("------------------------------------------------")
                print("Operação cancelada.")
                print("------------------------------------------------")
            else:
                saldo-=valor
                print("------------------------------------------------")
                print(f"Saque realizado no valor de R$ {valor:.2f}.")
                print("------------------------------------------------")
    elif resposta==3:
        print("------------------------------------------------")
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
        print("------------------------------------------------")

    elif resposta==4:
        break
    else:
        print("------------------------------------------------")
        print("Opção inválida")
        print("------------------------------------------------")