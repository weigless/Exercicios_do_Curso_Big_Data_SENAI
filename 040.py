#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma
# Sequência de Fibonacci


numero= int(input("Digite a quantidade de valores da sequência de Fibonacci que deseja exibir: "))

i=0
ant=0
atual=0

while i<numero:

    if i==0:
        atual=0

    if i==1 or i==2:
        ant= 0
        atual= 1

    proximo= ant+atual
    ant= atual
    atual= proximo

    i +=1
    print(atual)

