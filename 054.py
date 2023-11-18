'''Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

Apenas os 3 primeiros mais assistidos
Os últimos 2 mais assistidos
A lista em ordem alfabética
Em que posição está “O rei leão”
'''

Filmes_Mais_Assistidos= ('Avatar', 'Vingadores: Ultimato', 'Titanic', 'Star Wars: O Despertar da Força', 'Vingadores: Guerra Infinita', 'Jurassic World', 'O Rei Leão', 'Os Vingadores', 'Velozes & Furiosos 7', 'Frozen II')

print('\nOs 3 filmes mais assistidos:')
p=1
for count in range(0, 3):
   print(f'{p}º: {Filmes_Mais_Assistidos[count]}')
   p+=1

print('\n\nOs últimos 2 filmes mais assistidos:')
p=9
for count in range(8, 10):
   print(f'{p}º: {Filmes_Mais_Assistidos[count]}')
   p+=1


print(f'\n\nLista de Filmes mais assistidos em ordem alfabética:')
for i in sorted(Filmes_Mais_Assistidos):
    print(i)

#print(f'\n\nPosição em que o Filme Rei Leão aparece: {Filmes_Mais_Assistidos['O Rei Leão']}')
