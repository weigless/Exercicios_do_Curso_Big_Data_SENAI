# Desafio 01: Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

print("***** CLACULADORA DE POSIÇÃO NO MRUV")
S0= float(input("Informe a posição inicial do corpo: "))
V0= float(input("Informe a velocidade inicial do corpo: "))
A= float(input("Informe o valor da aceleração constante durante o movimento: "))
T= int(input("Informe o tempo de duração do movimento: "))
posicao= S0 + V0*T + (A*T**2)/2

print(f"A posição do objeto no tempo {T} é de {posicao} (m).")