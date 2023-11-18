#Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno

def area(a,b):
    area=a*b
    return area

while True:
    try:
        largura= float(input("Digite a largura do terreno em m: "))
        comprimento= float(input("Digite o comprimento do terreno em m: "))
        print(f"Área total do terreno: {area(largura,comprimento)} m²")
        break

    except ValueError:
        print("Digite um valor válido.")
