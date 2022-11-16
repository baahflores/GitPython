"""# O mesmo professor dom desafio anterior quer sortear a ordem de apresentação de trabalho
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
Consultas: >>> https://pt.stackoverflow.com/questions/477768/como-fa%C3%A7o-para-sortear
-nomes-aleat%C3%B3rios-de-cada-lista-sem-repeti-los <<<
>>> https://pythonhoje.wordpress.com/2018/01/23/the-journey-begins/ <<<"""
import random
aluno1 = str(input('Escreva o nome do aluno 1: '))
aluno2 = str(input('Escreva o nome do aluno 2: '))
aluno3 = str(input('Escreva o nome do aluno 3: '))
aluno4 = str(input('Escreva o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('>> HORA DO SORTEIO <<')
ordem = random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}')
