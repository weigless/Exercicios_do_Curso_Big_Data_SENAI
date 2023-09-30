'''idade= 33
print(f'Minha idade é {idade}')

idade = input("Digite a sua idade: ")
print(f'Sua idade é {idade}')

N1= int(input("Digite um número: "))
N2= int(input("Digite um número: "))
soma= N1+N2
print(f"A soma de N1 e N2 é {soma}")

nome= 'Weigless'
sobrenome= 'Camargo'
Nome_Completo = nome + " " + sobrenome
print(Nome_Completo)


Nome= input("Digite seu nome: ")
Nome= Nome.strip() #Remove os espaços a direita e esquerda
print(f"O tamanho do seu nome é {len(Nome)}") #função LEN analisa o tamanho da String
print(f"A primeira letra do seu nome é: {Nome[0]}") #Analisa a primeira string
print(f"A última letra do seu nome é: {Nome[-1]}") #Analisa a primeira string

Nome= Nome.split() #Separa nossa string em lista
print(f"O primeiro nome é: {Nome[0]}") # Analisando o primeiro item da lista
print(f"O último nome é: {Nome[-1]}") # Analisando o último item da lista
Nome= "/".join(Nome) #Método que junta todos os elementos da string separados pelo que a gente quiser
print(Nome)'''

altura= float(input("Digite a sua altura: "))
if altura >= 1.5 and altura <=2:
    print("Você pode andar no brinquedo!")
elif altura >2:
    print("Você vai bater a cabeça! Está proibido.")
else:
    print("Você é muito pequeno, quem sabe ano que vem.")