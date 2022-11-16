"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto."""
preco = float(input('Qual o preço daquela bolsa dos sonhos? R$ '))
d = (preco - preco * 0.05)
print(f'Só hoje ela sairá com 5%, caindo de R${preco:.2} para R${d:.2f}. Agora ficou fácil levar!')
