#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.
def maior (a):
    if a > 0:
        print(f"O número {a} é positivo")
    elif a<0:
        print(f"O número {a} é negativo")
    else:
        print(f"O número {a} é neutro")

numero= float(input("Digite um número: "))
maior(numero)
