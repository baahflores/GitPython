#Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros.
m = float(input('Escolha uma distância em metros: '))
cm = (m*100)
mm = (m*1000)
print('Considerando que {:.2f} está em metro, convertendo ficará:'.format(m))
print('{:.0f} centimetros e \n{:.0f} milimetros'.format(cm, mm))
