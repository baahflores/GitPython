"""Escreva um programa que converta uma temperatura digitando em graus Celsius
e converta para graus Fahrenheit."""
c = float(input('Qual a temperatura atual na sua cidade em °C? '))
f = (c * 9 / 5) + 32
print(f'Se a temperatura atual é igual a {c:.1f}°C, em fahrenheit seria {f:,.1f}°F')
