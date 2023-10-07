# Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
# é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente
# (9 ou maior).

def media(a,b,c,d,e,f):

    if f<6:
        print(f"Média insuficiente: {f}")
    elif f>=6 and f<7:
        print(f"Média suficiente: {f}")
    elif f>=7 and f<9:
        print(f"Média boa: {f}")
    else:
        print(f"Média excelente: {f}")

n1= float(input("Digite a nota 1: "))
n2= float(input("Digite a nota 2: "))
n3= float(input("Digite a nota 3: "))
n4= float(input("Digite a nota 4: "))
n5= float(input("Digite a nota 5: "))
calculo_media= (n1+n2+n3+n4+n5)/5

media(n1,n2,n3,n4,n5,calculo_media)
