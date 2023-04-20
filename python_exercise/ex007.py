n = input('Nome do docente?')
b1 = int(input('Nota do primeiro Semestre'))
b2 = int(input('Nota do segundo Semestre'))
r = (b1+b2)/2
print('A média de {} é {}' .format(n, r))
if r >= 6:
    print('APROVADO')
else:
    print('REPROVADO')