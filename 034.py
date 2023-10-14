#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

soma=0
for i in range(1,10+1):
    n1= int(input(f"Digite o número {i}: "))
    if n1%2==0:
        soma=soma+n1
print(f"Soma total dos números pares: {soma}")