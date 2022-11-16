"""Crie um programa que leia um número real pelo teclado e mostre na sua tela a
porção inteira. Ex: Digite um número: 6.126
> O número 6.126 tem a parte inteira 6"""
import math
n = float(input('Digite um número: '))
print(f'O número é {n} e sua parte inteira é {math.trunc(n)}')
# Como se trata de apenas uma funçaõ importada, também podemos importar apenas a função desejada,
# sendo: "from math import trunc" após isso, no print não será preciso digitar mais "math; Assim
# como também podemos simplesmente digitar "format(n, int(n))"
