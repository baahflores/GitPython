"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""
n = int(input('Me diga um número qualquer: '))
print(' ' * 2)
if n % 2 == 0:
    print('>> O número escolhido {} é PAR!'.format(n))
else:
    print('>> O número escolhido {} é ÍMPAR!'.format(n))
