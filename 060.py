#Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números pares da lista.

numeros=[1,2,3,4,5,6,7,8,9,10]
pares=[]

for par in numeros:
    if par % 2 == 0:
        pares.append(par)
print(f'Números pares: {pares}')