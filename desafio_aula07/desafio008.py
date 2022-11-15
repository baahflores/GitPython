"""Escreva um programa que leia um valor em metros e o exiba convertido
em centímetros e milímetros."""
m = float(input('Escolha uma distância em metros: '))
cm = (m*100)
mm = (m*1000)
print(f'Considerando que {m:.2f} está em metro, convertendo ficará:')
print(f'{cm:.0f} centimetros e \n{mm:.0f} milimetros')
