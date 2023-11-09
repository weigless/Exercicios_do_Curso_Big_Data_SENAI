#Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário 
#digitar 0000. No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

soma=0
total=0

while True:
    num=int(input("Digite um número inteiro ou 0000 para SAIR: "))
    soma+=num
    total+=1
    if num==0000:
        break
print(f"Total de números digitados: {total-1}\n"
      f"Soma total: {soma}")