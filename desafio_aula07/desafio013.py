"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 
15% de aumento"""
s = float(input('Quanto você está ganhando hoje? R$ '))
sn = (s + s * 0.15)
print('Tenho uma ótima novidade, conseguimos um aumento de 15% para você!')
print(f'Seu salário, que antes era de R${s:.2f}, agora irá para R${sn:.2f}')
