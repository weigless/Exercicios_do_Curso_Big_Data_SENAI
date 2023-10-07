#Escreva um programa que peça ao usuário uma senha e verifique se ela
# está correta (a senha correta é "python123").

def senha(a):
    if a=="python123":
        print("Acesso liberado!")
    else:
        print("Senha incorreta!")

palavra= input("Digite a senha: ")
senha(palavra)