"""Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa"""


n1= float(input(f"Digite o primeiro número: "))
n2= float(input("Digite o segundo número: "))
n3= float(input("Digite o terceiro número: "))

maior=0
resposta= ""

while resposta!= 5:
    print("MENU\n"
          "[1] Somar\n"
          "[2] Multiplicar\n"
          "[3] Maior\n"
          "[4] Novos números\n"
          "[5] Sair do programa")
    resposta = int(input("Escolha uma opção: "))
    if resposta==1:
        soma=n1+n2+n3
        print("\n------------------------------------------------")
        print(f"O resultado da soma de {n1} + {n2} + {n3} = {soma}")
        print("------------------------------------------------")
    elif resposta==2:
        multi=n1*n2*n3
        print("\n------------------------------------------------")
        print(f"O resultado da multiplicação de {n1} x {n2} x {n3} = {multi}")
        print("------------------------------------------------")
    elif resposta==3:
        if n1>n2 and n1>n3:
            maior=n1
        elif n2>n1 and n2>n3:
            maior=n2
        else:
            maior=n3
        print("\n------------------------------------------------")
        print(f"O maior número digitado é = {maior}")
        print("------------------------------------------------")
    elif resposta==4:
        n1 = float(input(f"Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        n3 = float(input("Digite o terceiro número: "))
    else:
        print("\n------------------------------------------------")
        print("Fim do Programa")
        print("------------------------------------------------")




