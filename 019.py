#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.
def intervalo(a):
    if a >=0 and a <=10:
        print("O número digitado está entre 0 e 10!")
    elif a > 10 and a<=20:
        print("O número digitado está entre 10 e 20!")
    else:
        print("O número digitado é maior do que 20!")


numero=float(input("Digite um número: "))
intervalo(numero)