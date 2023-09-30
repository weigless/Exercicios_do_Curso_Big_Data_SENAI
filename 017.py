#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
def vogal_ou_consoante(a):
    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
        print(f"A letra {a} é vogal!")
    else:
        print(f"A letra {a} é consoante!")



letra= input("Digite uma letra: ")
vogal_ou_consoante(letra)