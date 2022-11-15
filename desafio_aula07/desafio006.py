"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""
n = int(input('Escolha outro número: '))
dob = (n*2)
tri = (n*3)
rq = (n**(1/2))
print(f'O dobro de {n} é igual a {dob}.\nO triplo de {n} é igual a {tri}.')
print(f'E a raiz quadrada de {n} é igual {rq:.2f}')
print('Lembrando que também podemos criar o código usando uma mesma variável')
