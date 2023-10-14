# Escreva um programa que leia o
# Nome, idade e sexo de 4 pessoas. No final mostre:
#
# A média de idade do grupo
# Qual é o homem mais velho
# Quantas mulheres têm menos de 20 anos


soma_idade=0
feminino=0
idade_mais_velho=0
homem_mais_velho=""


for i in range (1,4+1):
    nome= input(f"Digite o nome da pessoa {i}: ")
    idade= int(input(f"Digite a idade da pessoa {i}: "))
    sexo= input(f"Digite o sexo para a pessoa {i} (M/F): ").upper()

    soma_idade=idade+soma_idade

    if sexo == "M" and idade > idade_mais_velho:
        idade_mais_velho = idade
        homem_mais_velho = nome
    elif sexo=="F" and idade<20:
        feminino= feminino+1


print(f"\nMédia de idade do grupo: {soma_idade/4}")
print(f"\nQuantidade de mulheres com menos de 20 anos: {feminino}")
print(f"\nO homem mais velho é {homem_mais_velho}, com a idade de {idade_mais_velho} anos")

