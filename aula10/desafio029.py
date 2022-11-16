#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
# acima do limite.
vel = float(input('Qual é a velocidade do carro? '))
print(' ' * 2)
excedido = vel - 80
multa = excedido * 7
if vel <= 80.0:
    print(f'Parabéns você passou com {vel} km/h dentro do limite de velocidade permitida!\n'
          'TENHA UM BOM DIA!')
else:
    print(f'Você foi multado, passou acima da velocidade em {excedido} km/h.\n'
          f'Por isso sua multa é de R${multa:.2f}.\nTENHA MAIS CUIDADO, DIRIJA COM SEGURANÇA!')
