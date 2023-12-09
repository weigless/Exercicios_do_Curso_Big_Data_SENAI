'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta'''

from random import randint

try:
    quantidade = int(input('Quantos jogos você quer gerar?: '))

    #Palpites
    palpites=[]

    for i in range(quantidade):
        numeros=[]
        while len(numeros) < 6:
            numero = randint(1,60)
            if numero not in numeros:
                numeros.append(numero)

        palpites.append(numeros[:])

    #Mostrar os resultados
    print(f'Foram gerados {quantidade} palpites de Mega Sena')
    for i,palpite in enumerate(palpites):
        numeros= ', '.join(str(numero) for numero in sorted(palpite))
        print(f'Jogo {i+1}: {numeros}')

except ValueError:
    print("Só aceitamos números.")