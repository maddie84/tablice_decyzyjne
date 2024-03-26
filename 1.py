from collections import Counter
import math


# Wczytaj dane z pliku tekstowego
nazwa_pliku = "gielda.txt"

with open(nazwa_pliku, 'r') as plik:
    linie = plik.readlines()

# Wstawia pierwszy wiersz jako nagłówki kolumn
linie.insert(0, "a1,a2,a3,a4\n")

# Rozdziel dane na wiersze i kolumny - tworzy listę `dane` zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
dane = [wiersz.strip().split(',') for wiersz in linie]

# Słownik z kolumnami
diction = {}
for i, kolumna in enumerate(dane[0]):
    diction[f'a{i + 1}'] = [wiersz[i] for wiersz in dane[1:]]


# Funkcja obliczająca entropię
def oblicz_entropie(data):
    total_count = len(data)
    class_counts = Counter(data)
    entropia = 0
    for count in class_counts.values():
        probability = count / total_count
        entropia -= probability * math.log2(probability) if probability > 0 else 0
    return entropia


# Funkcja obliczająca informację atrybutu
def oblicz_info_atrybutu(atrybuty, decyzje):
    liczba_obserwacji = len(atrybuty)
    licznik_atrybutow = Counter(atrybuty)
    info_atrybutu = 0
    for wartosc_atrybutu, liczba_wystapien in licznik_atrybutow.items():
        prawdopodobienstwo_atrybutu = liczba_wystapien / liczba_obserwacji
        podzbior_decyzji = [decyzje[i] for i in range(liczba_obserwacji) if atrybuty[i] == wartosc_atrybutu]
        licznik_decyzji = Counter(podzbior_decyzji)
        for liczba_wystapien_decyzji in licznik_decyzji.values():
            prawdopodobienstwo_decyzji = liczba_wystapien_decyzji / liczba_wystapien
            info_atrybutu -= prawdopodobienstwo_atrybutu * prawdopodobienstwo_decyzji * math.log2(prawdopodobienstwo_decyzji) if prawdopodobienstwo_decyzji > 0 else 0
    return info_atrybutu


# Funkcja obliczająca przyrost
def obliczenie_przyrostu(entropia, info):
    przyrost = entropia - info
    return przyrost

# Funkcja obliczająca GainRatio
def gainratio(przyrost, splitinfo):
    return przyrost / splitinfo if splitinfo != 0 else 0

# Funkcja rekurencyjnie tworząca drzewo decyzyjne
def create_decision_tree(data, atrybuty, decyzje):
    # Oblicz entropię całej kolumny decyzyjnej
    entropia_calkowita = oblicz_entropie(decyzje)

    # Wybierz atrybut z największym GainRatio
    max_gainratio = 0
    best_attribute = None
    for atrybut in atrybuty:
        info_atrybutu = oblicz_info_atrybutu(data[atrybut], decyzje)  # Poprawiono indeksowanie
        splitinfo = oblicz_entropie(data[atrybut])  # Poprawiono indeksowanie
        gain = obliczenie_przyrostu(entropia_calkowita, info_atrybutu)
        gainratio_atrybutu = gainratio(gain, splitinfo)
        if gainratio_atrybutu > max_gainratio:
            max_gainratio = gainratio_atrybutu
            best_attribute = atrybut

    # Stwórz węzeł drzewa
    wezel = {}
    wezel["atrybut"] = best_attribute

    # Podziel dane na podzbiory
    podziały = {}
    for wartosc_atrybutu in set(data[best_attribute]):
        podziały[wartosc_atrybutu] = {
            "atrybuty": [],
            "decyzje": []
        }
        for i, wartosc in enumerate(data[best_attribute]):
            if wartosc == wartosc_atrybutu:
                podziały[wartosc_atrybutu]["atrybuty"].append(data[best_attribute][i])
                podziały[wartosc_atrybutu]["decyzje"].append(decyzje[i])

    # Rekursywne tworzenie poddrzew
    for wartosc_atrybutu, podzial in podziały.items():
        wezel[wartosc_atrybutu] = create_decision_tree(podzial["atrybuty"], atrybuty.copy(), podzial["decyzje"])

    return wezel

# Uruchom funkcję
atrybuty_wszystkie = [0,1,2]
drzewo_decyzyjne = create_decision_tree(dane, atrybuty_wszystkie, 3)

# Funkcja do wyświetlania drzewa decyzyjnego w formie czytelnej dla człowieka
def print_decision_tree(tree, indent=''):
    if isinstance(tree, dict):
        for key, value in tree.items():
            if isinstance(value, dict):
                print(indent + str(key))
                print_decision_tree(value, indent + '  ')
            else:
                print(indent + str(key) + ': ' + str(value))
    else:
        print(indent + str(tree))

# Wyświetl drzewo decyzyjne
print_decision_tree(drzewo_decyzyjne)

