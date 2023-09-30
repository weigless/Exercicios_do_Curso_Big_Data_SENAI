'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas
2- O nome com todas minúsculas
3- Quantas letras ao todo (sem considerar os espaços)
4- Quantas letras tem o primeiro nome
OBS: Tratar os espaços extras entre os nomes
'''
nome= input("Digite o seu nome completo: ").strip()
print(f"Nome com todas as letras maiúsculas: {nome.upper()}"
      f"\nNome com todas as letras minúsculas: {nome.lower()}"
      f"\nQuantidade de letras: {len(nome.replace(' ',''))} letras")
nome=nome.split()
print(f"Quantidade de letras do primeiro nome: {len(nome[0])} letras")
