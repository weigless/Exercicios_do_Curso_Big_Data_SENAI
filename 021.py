# Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da
# semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).


def dia_da_semana(a):
    dia=["Domingo","Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]
    print(f"Dia da semana: {dia[a-1]}")

numero= int(input("Digite um número de 1 a 7: "))
dia_da_semana(numero)