#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores

soma=0
menor= 999999999999999999999999999999
maior= -99999999999999999999999999999
resposta=""
media=0
contador= 0

while resposta!="N":
    numero=int(input("Digite um número: "))
    soma+=numero
    contador+=1
    media = soma / contador
    if numero>maior:
        maior=numero
    elif numero<menor:
        menor=numero
    resposta=input("Deseja adicionar mais números? (S/N)").upper().strip()
print("\n------------------------------------------------")
print(f"A média dos números digitados é de: {media}\n"
      f"O maior número digitado foi: {maior}\n"
      f"O menor número digitado foi: {menor}")
print("------------------------------------------------")