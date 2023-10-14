#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

n1= int(input("Informe um número: "))
print(f"TABUADA DO NÚMERO {n1}")
for contador in range(0,10+1):
    print(f"{contador} x {n1}: {contador*n1}")