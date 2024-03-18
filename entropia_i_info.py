from collections import Counter
import math
from prettytable import PrettyTable

# Wczytaj dane z pliku tekstowego
nazwa_pliku = "test.txt"

with open(nazwa_pliku, 'r') as plik:
    linie = plik.readlines()

# wstawia pierwszy wiersz jako naglowki kolumn
linie.insert(0, "a1,a2,a3,a4,a5\n")

# Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
dane = [wiersz.strip().split(',') for wiersz in linie]

ind = 0
atr = 0
diction = {}
for i in dane[0]:
    ind = dane[0].index(i)
    atr = [wiersz[ind] for wiersz in dane[1:]]
    diction[f'a{ind + 1}'] = atr

def obliczenie_entropii(data):
    total_count = len(data) # ilosc wszystkich decyzji
    class_counts = Counter(data) # counter zlicza wystąpienia unikalnych elementow w liscie data ktora zawiera decyzje
    #print (f"class_count:{class_counts}") - 'down': 5, 'up': 5
   
    entropia = 0
    for count in class_counts.values():     # petla for przechodzi 2 razy,  raz dla 'down' i raz dla 'up', obliczając entropię dla każdej z tych klas. Wartości count będą wynosić 5 dla 'down' i 5 dla 'up' w dwóch osobnych iteracjach.
        probability = count / total_count
        entropia -= probability * math.log2(probability) if probability > 0 else 0

    return entropia

# Funkcja do obliczania informacji atrybutu
def oblicz_info_atrybutu(atrybuty, decyzje): #bierze tylko wartosci z kolumny atrybotow np a1 i decyzje do nich
    liczba_obserwacji = len(atrybuty) # ilosc wszystkich atrybutow
    licznik_atrybutow = Counter(atrybuty) # czyli tu bedzie np. 'old' : 3, 'mid' : 4, 'new' : 3
    info_atrybutu = 0

    for wartosc_atrybutu, liczba_wystapien in licznik_atrybutow.items(): # np. for mid, 4
        prawdopodobienstwo_atrybutu = liczba_wystapien / liczba_obserwacji
        # robimy liste decyzji dla dane wartosci, przechodzimy po wszystkich wierszach i bierzemy decyzje sprawdzajac ifem czy wartosc atrybutu np jest mid
        podzbior_decyzji = [decyzje[i] for i in range(liczba_obserwacji) if atrybuty[i] == wartosc_atrybutu]
        licznik_decyzji = Counter(podzbior_decyzji)
        #print(licznik_decyzji) #- np dla mid - Counter({'down': 2, 'up': 2})

        for liczba_wystapien_decyzji in licznik_decyzji.values(): # czyli np dla mid 2 przejscia petli for, najpierw for 2 in value=down i potem for 2 in value=up
            prawdopodobienstwo_decyzji = liczba_wystapien_decyzji / liczba_wystapien
            info_atrybutu -= prawdopodobienstwo_atrybutu * prawdopodobienstwo_decyzji * math.log2(prawdopodobienstwo_decyzji) if prawdopodobienstwo_decyzji > 0 else 0

    return info_atrybutu

def obliczenie_przyrostu(entropia, info):
    przyrost = entropia - info
    return przyrost

def gainratio(przyrost, splitinfo):
    return przyrost/splitinfo

# # Utwórz PrettyTable i dodaj kolumny
# tabela = PrettyTable(dane[0])
# for wiersz in dane[1:]:
#     tabela.add_row(wiersz)

# # Wyświetl wynik w formie tabeli
# print("\nDane:")
# print(tabela)

entropia = obliczenie_entropii(diction['a5'])
print(f"\nEntropia: {entropia:.4f}")

info_a1 = oblicz_info_atrybutu(diction['a1'], diction['a5'])
info_a2 = oblicz_info_atrybutu(diction['a2'], diction['a5'])
info_a3 = oblicz_info_atrybutu(diction['a3'], diction['a5'])

gain_a1 = obliczenie_przyrostu(entropia,info_a1)
gain_a2 = obliczenie_przyrostu(entropia,info_a2)
gain_a3 = obliczenie_przyrostu(entropia,info_a3)

splitinfo_a1 = obliczenie_entropii(diction['a1'])
splitinfo_a2 = obliczenie_entropii(diction['a2'])
splitinfo_a3 = obliczenie_entropii(diction['a3'])

gainratio_a1 = gainratio(gain_a1,splitinfo_a1)
gainratio_a2 = gainratio(gain_a2,splitinfo_a2)
gainratio_a3 = gainratio(gain_a3,splitinfo_a3)

# Wyświetl wyniki
print(f"Info(a1,T): {info_a1:.4f}, Gain(a1,T): {gain_a1}, GainRatio: {gainratio_a1}")
print(f"Info(a2,T): {info_a2:.4f}, Gain(a2,T): {gain_a2}, GainRatio: {gainratio_a2}")
print(f"Info(a3,T): {info_a3:.4f}, Gain(a3,T): {gain_a3}, GainRatio: {gainratio_a3}")
