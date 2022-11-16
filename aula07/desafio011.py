"""#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
 e a quantidade de tinta necessária para pintá-la, # sabendo que cada litro de tinta
 pinta uma área de 2 metros quadrados."""
pa1 = float(input('Qual largura da parede? '))
pa2 = float(input('Qual altura da parede? '))
area = (pa1 * pa2)
t = (area / 2)
print(f'Se cada litro de tinta pintar 2m², e sua parede tem as dimensões {pa1}x{pa2}m')
print(f'A área da sua parede é de {area:.1f}m². Você irá precisar de {t:.1f}L de tintas')
