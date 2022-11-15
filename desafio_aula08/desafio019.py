"""Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome dos escolhidos.
>>> https://gist.github.com/gabrielcesar/ee759ed4c2058608a690 <<<
>>> https://gist.github.com/gabrielcesar/ee759ed4c2058608a690 <<<"""
import random
aluno1 = str(input('Escreva o primeiro nome do aluno: '))
aluno2 = str(input('Escreva o segundo nome do aluno: '))
aluno3 = str(input('Escreva o terceiro nome do aluno: '))
aluno4 = str(input('Escreva o quarto nome do aluno: '))
pessoas = [aluno1, aluno2, aluno3, aluno4]
# >> Listas precisam ficar em [] <<
print('>> HORA DO SORTEIO <<')
sorteado = random.choice(pessoas)
print(f'O aluno escolhido foi: {sorteado}')
# Poderia ter importado apenas a função escolhida: "choice"
