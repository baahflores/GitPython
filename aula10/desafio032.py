"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
Para verificar se um ano é bissexto em Python, basta importar o módulo calendar .
Ele possuí uma função chamada isleap , que retorna True se o ano for bissexto."""
from datetime import date
print('=__' * 18)
n = int(input('Coloque 0 para analisar o ano atual, ou \ndigite um ano qualquer e descubra se ela bissexto: '))
print('=__' * 20)
print(' ')
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'Parabéns! O ano {n} é um ano BISSEXTO!')
else:
    print(f'Não foi dessa vez! O ano {n} não um ano BISSEXTO!')
