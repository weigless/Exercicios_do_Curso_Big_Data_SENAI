#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar
def par_ou_impar(a):
    if a%2==0:
        print(f"O número {a} é par")
    else:
        print(f"O número {a} é ímpar")

numero=float(input("Digite um número: "))
par_ou_impar(numero)
