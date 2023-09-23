#Exercicio 03: Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

print("***** MOSTRADOR DE NOME COMPLETO *****")
nome= input("Digite o seu nome: ")
sobrenome= input("Digite o seu sobrenome: ")
nome_completo= nome + " " + sobrenome
print(f"Seu nome completo é {nome_completo}")