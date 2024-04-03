from collections import Counter
import math

def wczytaj_dane1(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        linie = plik.readlines()

    # Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
    dane = [wiersz.strip().split(',') for wiersz in linie]
    
    return dane


def obliczenie_entropii1(data, atrybut):
    total_count = len(data)  # ilość wszystkich decyzji
    class_column = [row[atrybut] for row in data]  # kolumna zawierająca klasy decyzyjne
    class_counts = Counter(class_column)  # counter zlicza wystąpienia unikalnych elementów w liście klas decyzyjnych

    entropia = 0
    for count in class_counts.values():
        probability = count / total_count
        entropia -= probability * math.log2(probability) if probability > 0 else 0

    return entropia


def oblicz_info_atrybutu1(atrybuty, decyzje): #bierze tylko wartosci z kolumny atrybotow np a1 i decyzje do nich
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
    if (splitinfo == 0):
        gainratio = 0
    else:
        gainratio = przyrost/splitinfo
    return gainratio

dane = wczytaj_dane1("car.data")

entropia1 = obliczenie_entropii1(dane,-1)
atrybuty1 = [row[0] for row in dane]  # Pierwsza kolumna zawiera atrybuty (np. 'a1')
atrybuty2 = [row[1] for row in dane]
atrybuty3 = [row[2] for row in dane]
decyzje = [row[-1] for row in dane]  # Ostatnia kolumna zawiera decyzje

info_a1 = oblicz_info_atrybutu1(atrybuty1, decyzje)
info_a2 = oblicz_info_atrybutu1(atrybuty2, decyzje)
info_a3 = oblicz_info_atrybutu1(atrybuty3, decyzje)
# info_a4 = oblicz_info_atrybutu(atrybuty1, decyzje)

gain_a1 = obliczenie_przyrostu(entropia1,info_a1)
gain_a2 = obliczenie_przyrostu(entropia1,info_a2)
gain_a3 = obliczenie_przyrostu(entropia1,info_a3)
# gain_a4 = obliczenie_przyrostu(entropia,info_a4)

splitinfo_a1 = obliczenie_entropii1(dane, 0)
splitinfo_a2 = obliczenie_entropii1(dane, 1)
splitinfo_a3 = obliczenie_entropii1(dane, 2)
# splitinfo_a4 = obliczenie_entropii(diction['a4'])

gainratio_a1 = gainratio(gain_a1,splitinfo_a1)
gainratio_a2 = gainratio(gain_a2,splitinfo_a2)
gainratio_a3 = gainratio(gain_a3,splitinfo_a3)
# gainratio_a4 = gainratio(gain_a4,splitinfo_a4)

# # Wyświetl wyniki
# print(f"\nEntropia: {entropia1:.4f}")
# print(f"Info(a1,T): {info_a1:.4f}, Gain(a1,T): {gain_a1}, GainRatio: {gainratio_a1}")
# print(f"Info(a2,T): {info_a2:.4f}, Gain(a2,T): {gain_a2}, GainRatio: {gainratio_a2}")
# print(f"Info(a3,T): {info_a3:.4f}, Gain(a3,T): {gain_a3}, GainRatio: {gainratio_a3}")
