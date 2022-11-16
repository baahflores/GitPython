"""#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar."""
ct = float(input('Quanto você tem na carteira hoje? R$ '))
dl = (ct/3.27)
print(f'Com R${ct:.2f}, é possível comprar até US${dl:.2f}')
