from entropia_i_info import *
from collections import Counter
import math

dane = wczytaj_dane("gielda.txt")

atrybuty = list(dane.keys())[:-1]               # ['a1', 'a2', 'a3']

atrybut_decyzyjny = list(dane.keys())[-1]       # a4   

decyzje = dane[atrybut_decyzyjny]               # ['down', 'down', 'down', 'down', 'down', 'up', 'up', 'up', 'up', 'up']

# wszystkie_wartosci = Counter(value for values in dane.values() for value in values)     # Counter({'no': 6, 'swr': 6, 'down': 5, 'up': 5, 'mid': 4, 'yes': 4, 'hwr': 4, 'old': 3, 'new': 3})

def wybierz_najlepszy_atrybut(dane, decyzje, atrybuty):
    najlepszy_atrybut = None
    najlepszy_gainratio = -float('inf') # ujemna nieskonczonosc aby znaleźć wartość maksymalną dla gainratio atrybutow
    entropia = obliczenie_entropii(decyzje)

    for atrybut in atrybuty:
        info_atrybutu = oblicz_info_atrybutu(dane[atrybut], decyzje)
        przyrost = obliczenie_przyrostu(entropia, info_atrybutu)

        splitinfo = obliczenie_entropii(dane[atrybut])

        ratio = gainratio(przyrost, splitinfo)

        if ratio > najlepszy_gainratio:
            najlepszy_gainratio = ratio
            najlepszy_atrybut = atrybut

    return najlepszy_atrybut
