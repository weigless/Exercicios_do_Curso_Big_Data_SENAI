#Exercicio 05: Escreva um programa que converta real para o Franco Congolês

print("***** CONVERSOR DE MOEDA *****")
real= float(input("Digite o valor em real para conversão: "))
conversao= real*505.52

print(f"R${real:.2f} equivalem a {conversao:.2f} Francos Congoleses.")