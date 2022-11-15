#Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite Algo: ')
print('O tipo primitivo de {} é:'. format(a), type(a))
print('{} só tem espaços?'. format(a), (a.isspace()))
print('{} é numérico?'. format(a), (a.isnumeric()))
print('{} é alfabético?'. format(a), (a.isalpha()))
print('{} é alfanumérico?'. format(a), (a.isalnum()))
print('{} está em maiúsculo?'. format(a), (a.isupper()))
print('{} está em minúsculo?'. format(a), (a.islower()))
print('{} está capitalizado?'. format(a), (a.istitle()))
