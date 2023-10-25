#zad1
from random import randint
a = 1
b = 1
i = 0
j = 0
suma = 0
iloczyn = 1

while (a!=0):
    a = randint(-150, 150)
    i +=1
    if (a%2==0 and a>0):
        suma += a

while (j != i):
    b = randint(-10,10)
    j += 1
    if (b%2!=0 and b<0):
        iloczyn *= b

wynik = suma/iloczyn

print("Suma parzystych:",suma)
print("Iloczyn:",iloczyn)
print("Wynik:",wynik)

#zad2
lista = ["Ala i Ola", "Ala i Alan", "Asia ma kota", "Kolokwium fala"]
x = "Ala"
y = "Asia"

def konwersja(lista, a, b):
    i = 0
    konwersja = 0
    while i < len(lista):
        for x in lista[i]:
            lista[i] = lista[i].replace(a,b)
        i+=1
    return lista
            
print(konwersja(lista,x,y))




