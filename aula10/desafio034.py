"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""
s = float(input('Qual o seu salário atual? R$ '))
print(' ' * 1)
s_superior = (s * 0.10) + s
s_inferior = (s * 0.15) + s
print('Você recebeu um aumento!!! \o/')
if s <= 1250:
    print(f'Seu novo salário irá para R$ {s_inferior:.2f}')
else:
    print(f'Seu novo salário irá para R$ {s_superior:.2f}')
