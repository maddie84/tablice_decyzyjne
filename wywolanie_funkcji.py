from prettytable import PrettyTable
from entropia_i_info import *


with open("gielda.txt", 'r') as plik:
    linie = plik.readlines()
        
# wstawia pierwszy wiersz jako naglowki kolumn
linie.insert(0, "a1,a2,a3,a4\n")

# Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
dane = [wiersz.strip().split(',') for wiersz in linie]

# Słownik z kolumnami
diction = {}
for i, kolumna in enumerate(dane[0]):
    diction[f'a{i + 1}'] = [wiersz[i] for wiersz in dane[1:]]


entropia = obliczenie_entropii(diction['a4'])
print(f"\nEntropia: {entropia:.4f}")

info_a1 = oblicz_info_atrybutu(diction['a1'], diction['a4'])
info_a2 = oblicz_info_atrybutu(diction['a2'], diction['a4'])
info_a3 = oblicz_info_atrybutu(diction['a3'], diction['a4'])
# info_a4 = oblicz_info_atrybutu(diction['a4'], diction['a7'])

gain_a1 = obliczenie_przyrostu(entropia,info_a1)
gain_a2 = obliczenie_przyrostu(entropia,info_a2)
gain_a3 = obliczenie_przyrostu(entropia,info_a3)
# gain_a4 = obliczenie_przyrostu(entropia,info_a4)

splitinfo_a1 = obliczenie_entropii(diction['a1'])
splitinfo_a2 = obliczenie_entropii(diction['a2'])
splitinfo_a3 = obliczenie_entropii(diction['a3'])
# splitinfo_a4 = obliczenie_entropii(diction['a4'])

gainratio_a1 = gainratio(gain_a1,splitinfo_a1)
gainratio_a2 = gainratio(gain_a2,splitinfo_a2)
gainratio_a3 = gainratio(gain_a3,splitinfo_a3)
# gainratio_a4 = gainratio(gain_a4,splitinfo_a4)

# Wyświetl wyniki
print(f"Info(a1,T): {info_a1:.4f}, Gain(a1,T): {gain_a1}, GainRatio: {gainratio_a1}")
print(f"Info(a2,T): {info_a2:.4f}, Gain(a2,T): {gain_a2}, GainRatio: {gainratio_a2}")
print(f"Info(a3,T): {info_a3:.4f}, Gain(a3,T): {gain_a3}, GainRatio: {gainratio_a3}")
# print(f"Info(a4,T): {info_a4:.4f}, Gain(a4,T): {gain_a4}, GainRatio: {gainratio_a4}")

# # Utwórz PrettyTable i dodaj kolumny
# tabela = PrettyTable(dane[0])
# for wiersz in dane[1:]:
#     tabela.add_row(wiersz)

# # Wyświetl wynik w formie tabeli
# print("\nDane:")
# print(tabela)
