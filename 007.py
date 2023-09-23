#Exercicio 07: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print("***** DOBRO, TRIPLO E RAIZ QUADRADA *****")
n1= int(input("Digite um número: "))
dobro= n1*2
triplo= n1*3
raiz= n1**0.5

print(f"O dobro de {n1} é: {dobro}"
      f"\nO triplo de {n1} é: {triplo}"
      f"\nA raiz quadrade de {n1} é: {raiz:.2f}")
