#Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso

while True:
    try:
        extenso=('zero','um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze')

        numero=int(input('Digite um número de 0 a 15: '))

        print(f'{extenso[numero]}')
        break
    except IndexError:
        print('Você deve digitar um número de 0 a 15!')