'''Crie um programa que leia uma frase e mostre:
1- Quantas vezes aparece a letra “a”
2- Em que posição ela aparece na primeira vez
3- Em que posição ela aparece na última vez
'''
frase= input("Digite uma frase: ")
print(f"Quantidade de vezes que aparece a letra 'a': {frase.count('a')}")
print(f"Em que posição ela aparece na primeira vez: {frase.find('a')}º posição")
print(f"Em que posição ela aparece na última vez: {frase.rfind('a')}º posição")

