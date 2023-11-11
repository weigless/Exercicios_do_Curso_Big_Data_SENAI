"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
 o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""
import os


def caixa_eletronico():
    while True:
        try:
            print(" ***************** BEM-VINDO AO CAIXA ELETRÔNICO DO BANCO SENAI *****************\n")
            valor_saque = int(input("Digite o valor a ser sacado (ou digite 0 para sair): R$ "))

            if valor_saque == 0:
                print("Saindo do programa. Até mais!")
                break

            cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0

            cedulas_50 = valor_saque // 50
            valor_saque %= 50

            cedulas_20 = valor_saque // 20
            valor_saque %= 20

            cedulas_10 = valor_saque // 10
            valor_saque %= 10

            cedulas_1 = valor_saque

            print(f"\nCédulas de R$50: {cedulas_50}")
            print(f"Cédulas de R$20: {cedulas_20}")
            print(f"Cédulas de R$10: {cedulas_10}")
            print(f"Cédulas de R$1: {cedulas_1}")

        except ValueError:
            os.system("cls")
            print("Valor inválido!")


caixa_eletronico()