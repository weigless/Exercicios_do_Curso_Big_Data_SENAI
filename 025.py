#Crie um programa para jogar JOKEMPO, usando a função random.randint
# 1= TESOURA
# 2= PAPEL
# 3= PEDRA
import random
def JOKEMPO(a,b):
    lista=["TESOURA", "PAPEL", "PEDRA"]
    print(f"Você escolheu: {lista[a-1]}")
    print(f"O computador escolheu: {lista[b-1]}\n")
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        print("----> Você Ganhou <----")
    elif a==b:
        print("----> Empate <----")
    else:
        print("----> O computador ganhou <----")


Player_1=int(input("Escolha 1 para TESOURA, 2 para PAPEL ou 3 para PEDRA: "))
Player_2= random.randint(1,3)
JOKEMPO(Player_1,Player_2)
