"""Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase,
 coordenado por uma função


Exemplo:
       ----------------------------
            Senai Show de bola
       ----------------------------
"""

def titulo (frase, arg = '*'):
   print(arg * 2 * len(frase))
   print(f'{frase.center(len(frase) * 2)}')
   print(arg * 2 * len(frase))

frase= input('Digite a sua frase: ')
titulo(frase,'-')






