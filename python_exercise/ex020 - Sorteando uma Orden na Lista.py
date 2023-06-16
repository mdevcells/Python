print('-' * 28)
print('Sorteando uma Ordem na Lista')
print('-' * 28)
from random import shuffle
g1 = str(input('Primeiro grupo: '))
g2 = str(input('Segundo grupo: '))
g3 = str(input('Terceiro grupo: '))
g4 = str(input('Quarto grupo: '))
g5 = str(input('Quinto grupo: '))
lista = [g1, g2, g3, g4, g5]
ordem = shuffle(lista)
print('Ordem dos grupos: \n{}'.format(lista))