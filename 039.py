#Faça um programa que leia um número e retorne o fatorial !

numero= int(input("Digite um número: "))
fatorial = 1


while numero>0:
    fatorial= fatorial*numero
    numero=numero-1
print(fatorial)