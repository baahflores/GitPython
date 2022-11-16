"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""
nome = str(input('Digite seu nome completo: ')).strip()
# strip() tira os espaços antes e depois
print(f'Analisando seu {nome}...')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print('Seu nome {} tem {} letras no total'.format(nome, len(nome) - nome.count(' ')))
# Tamanho do nome - o número de espaços que tiver entre os nomes
listas = nome.split()
# Joga dentro de uma lista os nomes inteiros
print(listas)
print(f'Seu primeiro nome {listas[0]}, tem {len.listas[0]} letras')
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
