from math import sqrt, pow
cata = float(input('Digite o valor do cateto adjacente de um triangulo retangulo: '))
cato = float(input('Digite o valor do cateto oposto de um triangulo retangulo: '))
hipo = sqrt((pow(cata, 2)) + pow(cato, 2))
print('Cateto Adjacente: {} \n Cateto Oposto: {} \n Hipotenusa: {}'.format(cata, cato, hipo))