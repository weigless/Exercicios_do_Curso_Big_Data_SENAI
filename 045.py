"""Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000"""

while True:
    num=int(input("Digite um número ou 0000 para SAIR: "))
    if num == 0000:
        break
    print(f"----------Tabuada do número {num}----------")
    for i in range(0,11):
        print(f"{num} x {i}: {num*i}")
    
        
