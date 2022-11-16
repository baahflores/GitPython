"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele."""
a = input('Digite Algo: ')
print(f'O tipo primitivo de {a} é:'.type(a))
print(f'{a} só tem espaços?'.a.isspace())
print(f'{a} é numérico?'.a.isnumeric())
print(f'{a} é alfabético?'.a.isalpha())
print(f'{a} é alfanumérico?'.a.isalnum())
print(f'{a} está em maiúsculo?'.a.isupper())
print(f'{a} está em minúsculo?'.a.islower())
print(f'{a} está capitalizado?'.a.istitle())
