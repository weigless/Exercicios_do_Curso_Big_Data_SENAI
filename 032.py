#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

n1= int(input("Digite um número: "))
n2= int(input("Digite um número: "))

if n1%2==0:
    for contador in range(n1,n2+1,2):
        print(contador)
else:
    for contador in range(n1+1, n2+1, 2):
        print(contador)