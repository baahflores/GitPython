"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
h = ((co ** 2) + (ca ** 2)) ** (1 / 2)
print(f'O cateto oposto sendo {co:.2f} e o cateto adjacente sendo {ca:.2f}')
print('O tamanho da hipotenusa é igual a {h:.1f}')
# >> Também podemos importar: "h = math.hypot(co, ca) => dentro do módulo math <<
