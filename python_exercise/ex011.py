print('>>> Calculadora da area de Pintura <<<')
lg = float(input('Largura da parede:'))
al = float(input('Altura da parede:'))
vr = lg * al
vt = vr/2
print('\n >>> Area total da Pintura: {:.2f}m² \n >>> Litros de Tinta nescessario : {:.2f}l' .format(vr, vt))
