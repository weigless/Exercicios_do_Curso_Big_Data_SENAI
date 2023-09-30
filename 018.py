#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).
def maioridade(a):
    if a >=18:
        print("Parabéns, você já pode ser preso!")
    else:
        print("Cuidado, você pode ser encaminhado para a CASA")


idade= int(input("Digite a sua idade: "))
maioridade(idade)