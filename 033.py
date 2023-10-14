#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

soma = 0
for contador in range (1,500+1):
    if contador%4==0:
        soma+=contador
print(f"A soma dos múltiplos de 4 entre 1 e 100 é: {soma}")