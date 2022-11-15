"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""
p1 = float(input('Escolha um número entre 0 e 10: '))
p2 = float(input('Escolha mais um número entre 0 e 10: '))
m = (p1 + p2) / 2
print(f'Pedro tirou nas provas {p1:.1f} e {p2:.1f}. E sua média ficou igual a {m:.1f}')
