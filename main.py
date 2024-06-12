from bitwa import bitwaGlowna
from generatorBitw import bitwy, bitwySamWrog

t = 1
while t == 1:
    print("Co chcesz zrobić?")
    print("3 - Bitwa - generowanie 1000 rekordow samej armii wroga")
    print("2 - Bitwa - generowanie 1000 rekordow")
    print("1 - Bitwa")
    print("0 - zakoncz program")
    x = input("")
    try:
        x = int(x)
        if x == 1:
            bitwaGlowna()
        elif x == 2:
            bitwy(1000)
        elif x == 3:
            bitwySamWrog(1000)
        elif x == 0:
            t = 0
        else:
            print("Nie ma dostepnej opcji pod podanym numerem")
    except ValueError:
        print("Podales inny typ danych niz liczba")