"""Mas aqui ainda tem um erro, caso a pessoa não use com os 4 digitos"""
num = int(input('Digite um número: '))
n = str(num)
print(f'Analisando o número {num}')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centeza: {n[1]}')
print(f'Milhar: {n[0]}')