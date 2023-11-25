#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, deve mostrar para cada palavra, suas vogais

vogais=('a', 'e', 'i', 'o', 'u')
tupla= ('hoje', 'casa', 'rua')
for palavra in tupla:
    print(f'\n{palavra}')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')