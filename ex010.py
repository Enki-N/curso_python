larg = float(input('Digite o valor da largura da parede: '))
alt = float(input('Digite o valor da altura da parede: '))
area = larg * alt
print('A parede de {} por {} tem área igual a {}'.format(larg, alt, area))
print('E você precisará de {} litros de tinta para pinta-la'.format(area / 2))
