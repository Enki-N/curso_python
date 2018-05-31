dist = float(input('Digite a distancia de uma viagem em quilometros: '))

if dist < 200:
    preço = dist * 0.50
    print('Uma viagem de {:.2f}KM custa R${:.2f}'.format(dist, preço))
else:
    preço = dist * 0.45
    print('Uma viagem de {:.2f}KM custa R${:.2f}'.format(dist, preço))