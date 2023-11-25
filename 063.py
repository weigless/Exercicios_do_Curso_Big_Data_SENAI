'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta'''

abertos=0
fechados=0
lista=[]

frase= input("Digite a sua expressão: ")

for elemento in frase:
    if "(" in elemento:
        abertos+=1
        lista.append(elemento)

    if ")" in elemento:
        fechados+=1
        lista.append(elemento)

if abertos != fechados:
    print("O número de parênteses abertos e fechados devem ser o mesmo!")
elif lista[0] == ')':
    print("O primeiro parêntese não pode ser fechado!")
elif lista[-1] == '(':
    print("O último parêntese não pode ser aberto!")
else:
    print("Está certo!")