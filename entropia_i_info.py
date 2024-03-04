from collections import Counter
import math
from prettytable import PrettyTable

# Wczytaj dane z pliku tekstowego
nazwa_pliku = "gielda.txt"

with open(nazwa_pliku, 'r') as plik:
    linie = plik.readlines()

# wstawia pierwszy wiersz jako naglowki kolumn
linie.insert(0, "a1,a2,a3,decision\n")

# Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
dane = [wiersz.strip().split(',') for wiersz in linie]

# Pobierz indeks kolumny "decision" pierwszego wiersza (dane[0])
indeks_decision = dane[0].index('decision')

# Pobierz dane z kolumny "decision" (bez pierwszego wiersza, który zawiera nagłówki)
decyzje = [wiersz[indeks_decision] for wiersz in dane[1:]]

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

# Utwórz PrettyTable i dodaj kolumny
tabela = PrettyTable(dane[0])
for wiersz in dane[1:]:
    tabela.add_row(wiersz)

# Wyświetl wynik w formie tabeli
print("\nDane:")
print(tabela)

# Oblicz entropię dla kolumny "decision"
entropia = obliczenie_entropii(decyzje)
print(f"\nEntropia: {entropia:.4f}")

# Oblicz informacje atrybutów a1, a2, a3
indeks_a1 = dane[0].index('a1')
indeks_a2 = dane[0].index('a2')
indeks_a3 = dane[0].index('a3')

info_a1 = oblicz_info_atrybutu([wiersz[indeks_a1] for wiersz in dane[1:]], decyzje)
info_a2 = oblicz_info_atrybutu([wiersz[indeks_a2] for wiersz in dane[1:]], decyzje)
info_a3 = oblicz_info_atrybutu([wiersz[indeks_a3] for wiersz in dane[1:]], decyzje)

# Wyświetl wyniki
print(f"Info(a1,T):{info_a1:.4f}")
print(f"Info(a2,T):{info_a2:.4f}")
print(f"Info(a3,T):{info_a3:.4f}")
