"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar. No final mostre:

Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato"""


total_gasto=0
qtde_produtos_mais_1000=0
preco_produto_mais_barato=99999999999999999
produto_mais_barato=""

while True:
    nome=input("Digite o nome do produto: ")
    preco= float(input("Digite o preço do produto: R$ "))
    decisao= input("Deseja adicionar mais produtos? (S/N): ").strip().lower()

    total_gasto+=preco
    if preco > 1000:
        qtde_produtos_mais_1000+=1
    if preco<preco_produto_mais_barato:
        preco_produto_mais_barato=preco
        produto_mais_barato=nome
    if decisao=="n":
        break
print(f"Total gasto na compra: {total_gasto}\n"
      f"Quantidade de produtos que custam mais de R$1000,00: {qtde_produtos_mais_1000} produtos\n"
      f"Produto mais barato: {produto_mais_barato}")

        