"""Crie um programa que leia o nome de uma cidade diga se ela começa
ou não com o nome "SANTO"."""
city = str(input('Em qual cidade você nasceu? ')).strip()
"""Tirando espaços, antes e depois"""
print(city[:5].upper() == 'SANTO')
