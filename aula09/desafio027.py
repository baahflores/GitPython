# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# lista = [1, 2, 3, 4, 5]
# indice = len(lista) - 1
# print(indice)
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}\nSeu último nome é {}'.format(lista[0], lista[-1]))
#Ouu, print('Seu primeiro nome é {}\nSeu último nome é {}'.format(lista[0], nome[len(nome)-1]))
