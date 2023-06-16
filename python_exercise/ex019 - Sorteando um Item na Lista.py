print('-' * 23)
print('Lista de Sorteio')
print('-' * 23)
from random import choice
a1 = str(input('Primiero aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
lista = [a1, a2, a3, a4, a5]
sorteado = choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))