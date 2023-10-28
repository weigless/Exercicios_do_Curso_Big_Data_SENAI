#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário
# acerte o número. E no final, retorne também a quantidade de tentativas necessárias.
import random


sorte= random.randint(1,10)
tentativas= 0
numero=""

while numero != sorte:
    numero= int(input("Digite um número: "))
    tentativas+=1
print(f"Você acertou e precisou de {tentativas} tentativas")
