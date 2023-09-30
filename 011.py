'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas
2- O nome com todas minúsculas
3- Quantas letras ao todo (sem considerar os espaços)
4- Quantas letras tem o primeiro nome
'''

nome= input("Digite o seu nome completo: ").strip()
print(f"Nome completo com todas as letras maiúsculas: {nome.upper()}")
print(f"Nome completo com todas as letras maiúsculas: {nome.lower()}")
print(f"Quantidade de letras do Nome completo sem considerar os espaços: {len(nome.replace(' ', ''))}")

nome= nome.split()
primeiro_nome= nome[0]
print(f"Quantidade de letras do primeiro nome: {len(primeiro_nome)}")
