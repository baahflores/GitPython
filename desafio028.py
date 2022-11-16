"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""
import random
print(' ' * 15)
print('=__' * 15)
print('Vou pensar em um número entre 0 e 5. \nSerá que você é capaz de adivinhar?')
print('=__' * 15)
print(' ' * 15)
pc = random.randint(0, 5)
jogador = int(input('>>> Em qual número eu pensei? '))
print('PROCESSANDO...')
if pc == jogador:
    print('PARABÉNS VOCÊ ADIVINHOU!!!')
else:
    print('VOCÊ ERROU, TENTE OUTRA VEZ!!!')
