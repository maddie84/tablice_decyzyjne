from collections import Counter
import math
from entropia_i_info import obliczenie_entropii, oblicz_info_atrybutu, obliczenie_przyrostu, gainratio

# Wczytaj dane z pliku tekstowego
nazwa_pliku = "gielda.txt"

with open(nazwa_pliku, 'r') as plik:
    linie = plik.readlines()

# wstawia pierwszy wiersz jako naglowki kolumn
linie.insert(0, "a1,a2,a3,a4\n")

# Rozdziel dane na wiersze i kolumny - tworzy listę dane zawierającą wiersze, gdzie każdy wiersz jest listą kolumn
dane = [wiersz.strip().split(',') for wiersz in linie]

ind = 0
atr = 0
diction = {}
for i in dane[0]:
    ind = dane[0].index(i)
    atr = [wiersz[ind] for wiersz in dane[1:]]
    diction[f'a{ind + 1}'] = atr

# print(diction)

def build_decision_tree(data, attributes, decisions):
    # Jeśli wszystkie decyzje są takie same, zwracamy liść z tą decyzją
    if len(set(decisions)) == 1:
        return decisions[0]

    # Jeśli brak atrybutów lub osiągnięto warunek zakończenia, zwracamy najczęstszą decyzję
    if not attributes or len(data) < 2:
        return Counter(decisions).most_common(1)[0][0]

    best_attribute = None
    best_gain_ratio = -float('inf')
    
    # Obliczamy entropię dla całego zbioru decyzji
    total_entropy = obliczenie_entropii(decisions)

    for attribute_index in range(len(attributes)):
        attribute_values = [row[attribute_index] for row in data]
        # Obliczamy informację o atrybucie
        attribute_info = oblicz_info_atrybutu(attribute_values, decisions)
        # Obliczamy przyrost informacji
        gain = obliczenie_przyrostu(total_entropy, attribute_info)
        
        # Obliczamy split info dla współczynnika Gain Ratio
        split_info = obliczenie_entropii(attribute_values)
        
        # Obliczamy gain ratio
        gain_ratio = gainratio(gain, split_info)
        
        if gain_ratio > best_gain_ratio:
            best_gain_ratio = gain_ratio
            best_attribute = attribute_index

    # Podział danych na podzbiory na podstawie najlepszego atrybutu
    best_attribute_values = [row[best_attribute] for row in data]
    unique_attribute_values = set(best_attribute_values)
    
    subtree = {}
    for value in unique_attribute_values:
        new_data = []
        new_decisions = []
        new_attributes = attributes[:]
        for i in range(len(data)):
            if data[i][best_attribute] == value:
                new_data.append(data[i][:best_attribute] + data[i][best_attribute + 1:])
                new_decisions.append(decisions[i])
        subtree[value] = build_decision_tree(new_data, new_attributes, new_decisions)

    return {f'a{best_attribute + 1}': subtree}

def print_decision_tree(decision_tree, indent=''):
    if isinstance(decision_tree, dict):
        attribute = next(iter(decision_tree))
        print(indent + f"Atrybut: {attribute}")
        for key, subtree in decision_tree[attribute].items():
            print(indent + f"          {key} -> ", end='')
            print_decision_tree(subtree, indent + "       ")
    else:
        print(f"D: {decision_tree}")

# Tworzymy drzewo decyzyjne
decision_tree = build_decision_tree(dane[1:], list(range(len(dane[0]) - 1)), diction['a4'])

# Wyświetlamy drzewo decyzyjne
print_decision_tree(decision_tree)
