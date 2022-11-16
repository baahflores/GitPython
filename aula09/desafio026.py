"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
rfind => para começar pela direita/right"""
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
#Isso porque a numeração sempre começa pelo 0, então estamos dizendo que o 0 é a primeira letra!
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
