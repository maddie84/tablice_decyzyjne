from entropia_i_info import *
from collections import Counter
import math

def wybierz_najlepszy_atrybut(dane, decyzje, atrybuty):
    najlepszy_atrybut = None
    najlepszy_gainratio = -float('inf')
    entropia = obliczenie_entropii(decyzje)

    for atrybut in atrybuty:
        info_atrybutu = oblicz_info_atrybutu(dane[atrybut], decyzje)
        przyrost = obliczenie_przyrostu(entropia, info_atrybutu)

        # Obliczamy split info
        splitinfo = obliczenie_entropii(dane[atrybut])

        # Obliczamy gain ratio
        ratio = gainratio(przyrost, splitinfo)

        if ratio > najlepszy_gainratio:
            najlepszy_gainratio = ratio
            najlepszy_atrybut = atrybut

    return najlepszy_atrybut

def podziel_dane(dane, decyzje, atrybut_podzialu, wartosc_atrybutu):
    nowe_dane = {}
    nowe_decyzje = []

    for atrybut, wartosci in dane.items():
        nowe_dane[atrybut] = []
    for i, wartosc in enumerate(dane[atrybut_podzialu]):
        if wartosc == wartosc_atrybutu:
            nowe_decyzje.append(decyzje[i])
            for atrybut, wartosci in dane.items():
                nowe_dane[atrybut].append(wartosci[i])

    return nowe_dane, nowe_decyzje

def buduj_drzewo(dane, decyzje, atrybuty):
    if len(set(decyzje)) == 1:
        return decyzje[0]

    najlepszy_atrybut = wybierz_najlepszy_atrybut(dane, decyzje, atrybuty)

    drzewo = {najlepszy_atrybut: {}}
    atrybuty.remove(najlepszy_atrybut)

    for wartosc_atrybutu in set(dane[najlepszy_atrybut]):
        nowe_dane, nowe_decyzje = podziel_dane(dane, decyzje, najlepszy_atrybut, wartosc_atrybutu)
        drzewo[najlepszy_atrybut][wartosc_atrybutu] = buduj_drzewo(nowe_dane, nowe_decyzje, atrybuty[:])

    return drzewo

def print_drzewo(drzewo, wciecie=0):
    for key, value in drzewo.items():
        print(' ' * wciecie + str(key))
        if isinstance(value, dict):
            print_drzewo(value, wciecie + 2)
        else:
            print(' ' * (wciecie + 2) + str(value))


dane = wczytaj_dane("gielda.txt")
atrybuty = list(dane.keys())[:-1]
atrybut_decyzyjny = list(dane.keys())[-1]

atrybuty = list(dane.keys())[:-1]

decyzje = dane[atrybut_decyzyjny]  # Decyzja znajduje się w ostatniej kolumnie

drzewo = buduj_drzewo(dane, decyzje, atrybuty)  # Nie uwzględniamy ostatniej kolumny jako atrybutu

print_drzewo(drzewo)
