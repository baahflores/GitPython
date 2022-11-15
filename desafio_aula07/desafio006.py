#Crie um algoritmo que leia um número e mostre o seu dobro, triplo
# e raiz quadrada.
n = int(input('Escolha outro número: '))
dob = (n*2)
tri = (n*3)
rq = (n**(1/2))
print('O dobro de {} é igual a {}.\nO triplo de {} é igual a {}.'.format(n, dob, n, tri))
print('E a raiz quadrada de {} é igual {:.2f}'.format(n, rq))
print('Lembrando que também podemos criar o código usando uma mesma variável ♥')
