#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
b = float(input('Qual o preço daquela bolsa dos sonhos? R$ '))
d = (b - b * 0.05)
print('Só hoje ela sairá com 5%, caindo de R${:.2} para R${:.2f}. Agora ficou fácil levar!'.format(b, d))

