"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
valor_3 = int(input('Terceiro valor: '))
print(' ' * 2)
if valor_1 > valor_2 and valor_1 > valor_3:
    print(f'O maior valor é {valor_1}')
if valor_2 > valor_1 and valor_2 > valor_3:
    print(f'O maior valor é {valor_2}')
if valor_3 > valor_1 and valor_3 > valor_2:
    print(f'O maior valor é {valor_3}')
print(' ' * 2)
if valor_1 < valor_2 and valor_1 < valor_3:
    print(f'O menor valor é {valor_1}')
if valor_2 < valor_1 and valor_2 < valor_3:
    print(f'O menor valor é {valor_2}')
if valor_3 < valor_1 and valor_3 < valor_2:
    print(f'O menor valor é {valor_3}')
#Outro modo: https://www.pythonprogressivo.net/2018/10/Funcao-Mostra-Maior-Menor-Numero-Python.html
