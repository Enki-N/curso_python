sal = float(input('Digite o valor do seu salario: '))

if sal > 1250:
    novosal = sal + (sal * 0.1)
else:
    novosal = sal + (sal * 0.15)

print('O seu novo salario é de R${}'.format(novosal))