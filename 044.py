"""Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. 
Ao final deve mostrar a quantidade de vitórias"""
import random
import os

vitorias_usuario=0

while True:
    usuario_escolha= input("Escolha P (par) ou I (ímpar): ").strip().lower()
    usuario_num= int(input("Escolha um número entre 0 e 10: "))
    pc_num=random.randint(0,10)
    if usuario_escolha=="p" and (usuario_num + pc_num) %2==0:
        os.system("cls")
        print("-----------------------------------")
        print(f"Número escolhido pelo PC: {pc_num}")
        print("Você venceu!")
        print("-----------------------------------")
        vitorias_usuario+=1
    elif usuario_escolha=="i" and (usuario_num + pc_num +1) %2==0:
        os.system("cls")
        print("-----------------------------------")
        print(f"Número escolhido pelo PC: {pc_num}")
        print("Você venceu!")
        print("-----------------------------------")
        vitorias_usuario+=1
    else:
        os.system("cls")
        print("-----------------------------------")
        print(f"Número escolhido pelo PC: {pc_num}")
        print("PC ganhou!")
        print("-----------------------------------")
        break

print(f"Total de vitórias: {vitorias_usuario}")
   