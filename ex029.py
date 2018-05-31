vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    print('Acima da velocidade permitida \n Você foi multado em', end=' ')
    multa = (vel - 80) * 7
    print('R${}'.format(multa))
else:
    print('Esta dentro da velocidade permitida. Parabens!!')