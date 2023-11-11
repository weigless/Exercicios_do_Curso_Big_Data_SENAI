#Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo
# número. No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido,
# como uma string ou o número zero.


try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    print(f"Resultado da divisão: {numero_1/numero_2}")

except ZeroDivisionError:
    print("Não é possível dividir por 0.")

except ValueError:
    print("Você deve digitar um número válido.")