# Crie um programa que leia dois números e mostre a soma entre eles.
print('Vamos brincar um pouco? ')
a = int(input('Escolha um número entre 1 e 10: '))
b = int(input('Agora, escolha outro número entre 1 e 10: '))
s = (a + b)
print('Você escolheu {} e {}, e a soma entre esses números é de {}'.format(a, b, s))
a = int(input('Escolha um número entre 11 e 20: '))
b = int(input('Agora, escolha outro número entre 1 e 10: '))
print('Os números escolhidos foram', a, 'e', b, )
s = a + b
print('A soma dos números é de:', s, )
d = a - b
print('A diferença entre o maior número e o menor será de:', d, )
print('Agora um pouco diferente')
n1 = int(input('Escolha um número entre 10 e 20: '))
n2 = int(input('Agora, escolha outro número entre 1 e 10: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
