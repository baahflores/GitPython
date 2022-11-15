#Crie um programa que leia dois números e mostre a soma entre eles.
n = int(input('Escolha um número: '))
ant = (n-1)
suc = (n+1)
print('O antescessor é {} \n e o sucessor é {}'.format(ant, suc))
#Com outro código, agora usando apenas uma mesma variável, fica:
print('OBS: O fato de usar menos variáveis economiza a memória')
print('Analisando o valor {}, \nseu antescessor é {} e \nseu sucessor é {}'.format(n, (n-1), (n+1)))
