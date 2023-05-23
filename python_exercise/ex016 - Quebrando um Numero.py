print('-' * 20)
print('Exercício de Módulo')
print('-' * 20)
'''n = float(input('Digite um valor:'))
print('O valor foi: {} e sua porção inteira é: {}' .format(n, int(n)))'''

from math import trunc
n = float(input('Digite un valor:'))
print('Valor mensionado: {} sua porção inteira é: {}' .format(n, trunc(n)))
