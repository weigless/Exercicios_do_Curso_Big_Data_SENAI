#Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome= input("Digite o seu nome completo: ")
nome= nome.split()
print(f"Primeiro nome: {nome[0]}")
print(f"Último nome: {nome[-1]}")