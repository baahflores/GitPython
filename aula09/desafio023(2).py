"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
separados em unid, dez, cent, milhar, e assim por diante."""
num = int(input('Digite um número [0 a 9999]: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
"""
// -> div - coquiente da divisão inteira
 % -> mod - resto da divisão inteira"""
 
print(f'Analisando o número: {num}')
print(f'Analisando unidadde: {u}')
print(f'Analisando dezena: {d}')
print(f'Analisando centena: {c}')
print(f'Analisando milhar: {m}')
