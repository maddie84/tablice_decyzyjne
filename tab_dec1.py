licznik_wartosci = {}

with open('gielda.txt', 'r') as plik:
    # Iterujemy przez linie w pliku
    for linia in plik:
        # Usuwamy białe znaki z początku i końca linii, a następnie dzielimy linie na wartości przy użyciu przecinków
        wartosci = linia.strip().split(',')

        # Iterujemy przez wartości w danej linii
        for wartosc in wartosci:
            # Sprawdzamy, czy wartość już istnieje w słowniku
            if wartosc in licznik_wartosci:
                # Jeśli tak, zwiekszamy ilość
                licznik_wartosci[wartosc] += 1
            else:
                # Jeśli nie, dodajemy nowy klucz do słownika
                licznik_wartosci[wartosc] = 1

for klucz, wartosc in licznik_wartosci.items():
    print(f"{klucz}: {wartosc}")

print(licznik_wartosci)