"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas."""

viagem = float(input('Qual a distância da viagem em km? '))
v_curta = viagem * 0.5
v_longa = viagem * 0.45
print(' ' * 2)
if viagem <= 200:
    print(f'Para uma viagem de {viagem} km, sua passagem é de R$ {v_curta:.2f}.')
else:
    print(f'Para sua viagem de {viagem} km, sua passagem é de R$ {v_longa:.2f}.')

#Outro método: preço = viagem * 0.5 if viagem <= 200 else viagem * 0.45
