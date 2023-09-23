#Exercicio 08: Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.'''

print("***** CALCULADORA DE REAJUSTE DE SALÁRIO *****")
salario= float(input("Digite o seu salário atual: "))
reajuste= salario+(salario*0.6)

print(f"O salário de {salario} com o reajuste de 60% será de: {reajuste:.2f}")
