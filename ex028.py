import random
num = random.randint(0,5)
val = int(input('Digite um valor entre 0 e 5 e tente adivinhar que numero o computador escolheu: '))

if val == num:
    print('Parabens!! Você ganhou')
else:
    print('Errou!! O computador ganhou')
    print('O numero era o {}'.format(num))