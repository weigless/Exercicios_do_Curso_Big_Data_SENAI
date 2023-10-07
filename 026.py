# Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está
# entre a faixa ideal, acima ou abaixo do IMC ideal.

def imc(a,b,c):
    if c < 18.4:
        print(f"Seu IMC é de {c:.2f} e é considerado: ABAIXO DO PESO.")
    elif c >=18.5 and c <25:
        print(f"Seu IMC é de {c:.2f} e é considerado: PESO IDEAL.")
    else:
        print(f"Seu IMC é de {c:.2f} e é considerado: ACIMA DO PESO.")

peso= float(input("Digite o seu peso em kg: "))
altura= float(input("Digite a sua altura em m: "))
calculo_imc= peso/(altura**2)

imc(peso,altura,calculo_imc)