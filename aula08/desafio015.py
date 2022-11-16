"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0,15 por Km rodado."""
name = input('Qual o seu nome? ')
print(f'Prazer ter você aqui, {name}!')
km = float(input('Quantos km você percorreu com o carro? '))
kmp = km * 0.15
dias = int(input(f'E por quantos dias ele ficou alugado em seu nome, {name}? '))
diasa = dias * 60
print(f'Como para cada km percorrido é cobrado R$0.15 e você percorreu {km} km')
print(f'E como é cobrado R$60/dia, e você alugou por {dias} dias.')
print(f'Sua conta dá: R${kmp:.2f} por km rodados + R$ {diasa} por dias alugados')
t = kmp + diasa
print(f'Totalizando: R${t:.2f}. Aceitamos dinheiro, pix ou cartão. Como ficar melhor! ')
print('-' * 50)
print('-' * 50)
km = float(input('Quantos km você percorreu com o carro? '))
dias = int(input(f'E por quantos dias ele ficou alugado em seu nome, {name}? '))
pago = (dias * 60) + (km * 0.15)
print(f'{name}, o total a pagar é de R$ {pago:.2f}')
