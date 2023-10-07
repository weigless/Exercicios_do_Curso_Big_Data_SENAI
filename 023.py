#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.
def v_ou_c(a):
    vogal=["a","e","i","o","u"]
    if a[0] in vogal:
        print("A primeira letra da palavra é uma VOGAL")
    else:
        print("A primeira letra da palavra é uma CONSOANTE")

palavra= input("digite uma palavra: ").lower()
v_ou_c(palavra)