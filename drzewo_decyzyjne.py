from funkcje_lista import *
from buduj_drzewo import *


def wybierz_najlepszy_atrybut(dane):
    najlepszy_gainratio = 0
    najlepszy_atrybut = None
    entropia = obliczenie_entropii1(dane, -1)  # entropia dla całego zbioru danych
    decyzje = [row[-1] for row in dane]  # decyzje z ostatniej kolumny

    for idx in range(len(dane[0]) - 1):  # Iteruj po indeksach kolumn, pomijając ostatnią (decyzje)
        kolumna = [row[idx] for row in dane]  # kolumna odpowiadającą bieżącemu atrybutowi
        info_atrybutu = oblicz_info_atrybutu1(kolumna, decyzje)  
        przyrost = obliczenie_przyrostu(entropia, info_atrybutu)  
        
        splitinfo = obliczenie_entropii1(dane, idx)  
        
        ratio = gainratio(przyrost, splitinfo)

        if ratio > najlepszy_gainratio:
            najlepszy_gainratio = ratio
            najlepszy_atrybut = idx

    return najlepszy_atrybut

def podziel_dane(dane, indeks_atrybutu):
    podzielone_dane = {}
    
    for wiersz in dane:
        wartosc_atrybutu = wiersz[indeks_atrybutu]
        if wartosc_atrybutu not in podzielone_dane:
            podzielone_dane[wartosc_atrybutu] = []
        podzielone_dane[wartosc_atrybutu].append(wiersz)
    
    return podzielone_dane

def buduj_wezel(dane):
    wezel = {}
    najlepszy_atrybut_indeks = wybierz_najlepszy_atrybut(dane)
    if najlepszy_atrybut_indeks == None:
        decyzja = dane[0][-1]
        wezel = decyzja
    else:
        podzielone_dane = podziel_dane(dane, najlepszy_atrybut_indeks)
        wezel[najlepszy_atrybut_indeks] = {} 

        for atrybut in podzielone_dane:
            dane = podzielone_dane[atrybut]
            wezel[najlepszy_atrybut_indeks][atrybut] = buduj_wezel(dane)
    return wezel

# dane = wczytaj_dane1("car.data")
dane = wczytaj_dane1("testowaTabDec.txt")

drzewo = buduj_wezel(dane)

w = buduj(drzewo)
wyswietl_drzewo(w, 0)

