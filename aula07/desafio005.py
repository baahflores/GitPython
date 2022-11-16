"""Crie um programa que leia dois números e mostre a soma entre eles."""
n = int(input('Escolha um número: '))
ant = (n-1)
suc = (n+1)
print(f'O antescessor é {ant} \n e o sucessor é {suc}')
#Com outro código, agora usando apenas uma mesma variável, fica:
print('OBS: O fato de usar menos variáveis economiza a memória')
print(f'Analisando o valor {n}, \nseu antescessor é {n-1} e \nseu sucessor é {n+1}')
