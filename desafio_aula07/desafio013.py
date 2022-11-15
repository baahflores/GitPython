#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
#, com 15% de aumento
s = float(input('Quanto você está ganhando hoje? R$ '))
sn = (s + s * 0.15)
print('Tenho uma ótima novidade, conseguimos um aumento de 15% para você!')
print('Seu salário, que antes era de R${:.2f}, agora irá para R${:.2f}'.format(s, sn))