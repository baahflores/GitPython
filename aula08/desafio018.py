#Faça um programa que leia um ângulo e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
# >>>IMPORTANTE: https://docs.python.org/3/library/math.html <<<
import math
a = float(input('Digite o valor do ângulo para descobrir seu seno, cosseno e tangente: '))
# Precisa converter pois aqui mostra apenas o valor em RADIANOS
cos = math.cos(math.radians(a))
seno = math.sin(math.radians(a))
tan = math.tan(math.radians(a))
print(f'Analisando o valor {a}, temos: \nSeno igual a {seno:.2f}')
print(f'Cosseno igual a {cos:.2f} \nTangente igual a {tan:.2}')
# também podemos importar apenas "from math import radians, cos, sin, tan"
