#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.
def iguais_ou_dif(a,b):
     if a==b:
         print("Os números são iguais!")
     else:
         print("Os números são diferentes!")

num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
iguais_ou_dif(num1,num2)