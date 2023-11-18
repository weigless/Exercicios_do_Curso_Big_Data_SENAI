#Escreva um programa que tenha uma função, verifica_par(), que receba um número e verifique se é par

def verifica_par(numero):
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")

while True:
    try:
        numero= int(input("Digite um número: "))
        verifica_par(numero)
        break

    except ValueError:
        print("Número inválido.")