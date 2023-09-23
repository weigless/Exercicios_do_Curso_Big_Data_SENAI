#Exercicio 04: Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

print("***** CALCULADORA DE VOLUME E ÁREA DA ESFERA *****")
import math
raio= float(input("Digite o raio da esfera: "))
volume= (4/3)*math.pi*(raio**3)
area= 4*math.pi*(raio**2)

print(f"Volume da Esfera: {volume:.2f}"
      f"\nÁrea da Esfera: {area:.2f}")

