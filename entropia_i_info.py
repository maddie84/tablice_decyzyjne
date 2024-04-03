from collections import Counter
import math

def wczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        linie = plik.readlines()
        
    # wstawia pierwszy wiersz jako naglowki kolumn
    linie.insert(0, "a1,a2,a3,a4\n")

    # Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
    dane = [wiersz.strip().split(',') for wiersz in linie]

    # Słownik z kolumnami
    diction = {}
    for i, kolumna in enumerate(dane[0]):
        diction[f'a{i + 1}'] = [wiersz[i] for wiersz in dane[1:]]
    
    return diction

def wczytaj_dane1(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        linie = plik.readlines()

    # Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
    dane = [wiersz.strip().split(',') for wiersz in linie]
    
    return dane

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

