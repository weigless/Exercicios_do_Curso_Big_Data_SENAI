#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maior=0
menor=1000

for i in range(1,7+1):
    peso= float(input(f"Digite o peso da pessoa {i}: "))
    if peso> maior:
        maior=peso
    elif peso<menor:
        menor=peso
print(f"Maior peso: {maior}")
print(f"Menor peso: {menor}")