#Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.
p1 = float(input('Escolha um número entre 0 e 10: '))
p2 = float(input('Escolha mais um número entre 0 e 10: '))
m = (p1 + p2) / 2
print('Pedro tirou nas provas {:.1f} e {:.1f}. E sua média ficou igual a {:.1f}'.format(p1, p2, m))
