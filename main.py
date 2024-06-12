from bitwa import bitwaGlowna
from generatorBitw import bitwy

t = 1
while t == 1:
    print("Co chcesz zrobić?")
    print("2 - Bitwa - generowanie 1000 recordow")
    print("1 - Bitwa")
    print("0 - zakoncz program")
    x = input("")
    try:
        x = int(x)
        if x == 1:
            bitwaGlowna()
        elif x == 2:
            bitwy(1000)
        elif x == 0:
            t = 0
        else:
            print("Nie ma dostepnej opcji pod podanym numerem")
    except ValueError:
        print("Podales inny typ danych niz liczba")