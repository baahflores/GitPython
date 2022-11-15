#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.
ct = float(input('Quanto você tem na carteira hoje? R$ '))
dl = (ct/3.27)
print('Com R${:.2f}, é possível comprar até US${:.2f}'. format(ct, dl))
print('>>> Fazer agora conversão para euro e libra')
