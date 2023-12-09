#Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista, que mantenha separado as consoantes das vogais

vogais= ['a','e','i','o','u']
lista_vogais= list()
lista_consoantes= list()
lista_geral= list()

for i in range(0,6):
    letra= input("Digite uma letra: ")
    if letra in vogais:
        lista_vogais.append(letra)


    else:
        lista_consoantes.append(letra)

    lista_geral.append(lista_vogais[:])
    lista_geral.append(lista_consoantes[:])
    lista_consoantes.clear()
    lista_vogais.clear()

print(lista_vogais)
print(lista_consoantes)
print(lista_geral)


