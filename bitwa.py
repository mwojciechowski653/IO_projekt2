import random
import time


def losowanie_armii(x):
    armia = []
    for i in range(3):
        x = max(0, x)
        y = random.randint(1, (x+4)//2)
        z = random.randint(1, 3)
        if z == 1:
            typ = "konnica"
            x = x-y*2
            armia.append([typ, y])
        elif z == 2:
            typ = "piechurzy"
            x = x-y
            armia.append([typ, y])
        else:
            typ = "artylerzysci"
            x = x-y*1.5
            armia.append([typ, y])
    return armia


def walka(a, b):
    if a[0] == "piechurzy":
        if b[0] == "piechurzy":
            mnoznik = 1.0
        elif b[0] == "konnica":
            mnoznik = 0.5
        else:
            mnoznik = 0.5
    elif a[0] == "konnica":
        if b[0] == "piechurzy":
            mnoznik = 2.0
        elif b[0] == "konnica":
            mnoznik = 1
        else:
            mnoznik = 1.5
    else:
        if b[0] == "piechurzy":
            mnoznik = 2.0
        elif b[0] == "konnica":
            mnoznik = 0.75
        else:
            mnoznik = 1.0
    return mnoznik


def zwiad(budzet, zwiady, armia_przeciwnika):
    print("Możesz wydać 100 monet aby wysłać zwiad i dowiedzieć się jak wygląda jedno ze skrzydeł wroga (lub wiecej skrzydel 100monet = 1zwiad)")
    print("Czy chcesz to zrobić? (od 1 do 3) - Tak, podaj ile skrzydeł chcesz sprawdzić, 0 - Nie")
    odpowiedz = input()
    try:
        odpowiedz = int(odpowiedz)
        if odpowiedz < 0 or odpowiedz > 3:
            print("Nie ma takiej ilosci skrzydel")
        else:
            for i in range(odpowiedz):
                v = 1
                zwiady += 1
                while v == 1:
                    print("Ktore skrzydlo chcesz sprawdzic?")
                    print("1 - lewe, 2 - środek, 3 - prawe")
                    ktore = input()
                    try:
                        ktore = int(ktore)
                        if ktore == 1:
                            print(armia_przeciwnika[0])
                            budzet = budzet - 100
                            v = 0
                        elif ktore == 2:
                            print(armia_przeciwnika[1])
                            budzet = budzet - 100
                            v = 0
                        elif ktore == 3:
                            print(armia_przeciwnika[2])
                            budzet = budzet - 100
                            v = 0
                        else:
                            print("Podana liczba nie reprezentuje zadnego skrzydla!")
                    except ValueError:
                        print("Podales inny typ danych niz liczba")

    except ValueError:
        print("Podales inny typ danych niz liczba")
        return
    
    return budzet, zwiady


def obsadzanie_wojskiem(budzet, armia):
    for j in range(3):
        v = 1
        while v == 1:
            print("Masz do dyspozycji:", budzet, "złotych monet")
            if j == 0:
                print("Wybierz jaka jednostke chcesz na lewym skrzydle i jaka ona bedzie miala liczebnosc:")
            elif j == 1:
                print("Wybierz jaka jednostke chcesz na środku i jaka ona bedzie miala liczebnosc:")
            else:
                print("Wybierz jaka jednostke chcesz na prawym skrzydle i jaka ona bedzie miala liczebnosc:")
            print("Podaj typ jednostki: piechurzy/konnica/artylerzysci")
            typ_jednostki = input()
            print("Podaj jej liczebnosc:")
            liczebnosc = input()

            try:
                liczebnosc = int(liczebnosc)
                if typ_jednostki.lower() == "piechurzy":
                    if liczebnosc >= 0:
                        if liczebnosc > budzet:
                            print("Przekroczyles swoj budzet")
                        else:
                            armia.append([typ_jednostki.lower(), liczebnosc])
                            budzet = budzet - liczebnosc
                            v = 0
                    else:
                        print("Podana liczebnosc nie moze byc ujemna!")
                elif typ_jednostki.lower() == "artylerzysci":
                    if liczebnosc >= 0:
                        if liczebnosc * 1.5 > budzet:
                            print("Przekroczyles swoj budzet")
                        else:
                            armia.append([typ_jednostki.lower(), liczebnosc])
                            budzet = budzet - liczebnosc * 1.5
                            v = 0
                    else:
                        print("Podana liczebnosc nie moze byc ujemna!")
                elif typ_jednostki.lower() == "konnica":
                    if liczebnosc >= 0:
                        if liczebnosc * 2 > budzet:
                            print("Przekroczyles swoj budzet")
                        else:
                            armia.append([typ_jednostki.lower(), liczebnosc])
                            budzet = budzet - liczebnosc * 2
                            v = 0
                    else:
                        print("Podana liczebnosc nie moze byc ujemna!")
                else:
                    print("Zle podales typ jednostki!")
            except ValueError:
                print("Podana liczebnosc nie jest liczba!")


def bitwa(kierunek, armia, armia_przeciwnika):
    if kierunek == "lewo":
        print("Walka na lewym skrzydle")
        b = armia_przeciwnika[0]
        a = armia[0]
    elif kierunek == "prawo":
        print("Walka na prawym skrzydle")
        b = armia_przeciwnika[2]
        a = armia[2]

    print("Twoj oddzial:")
    print(a)
    print("Oddzial wroga:")
    print(b)
    time.sleep(3)
    print(".", end="")
    time.sleep(2)

    nasz_wspolczynnik = walka(a, b)
    print(".", end="")
    szczescie = random.randint(75, 125) * 0.01
    time.sleep(2)
    print(".")
    time.sleep(2)
    if a[1] * nasz_wspolczynnik * szczescie > b[1]:
        if kierunek == "lewo":
            print("Brawo! Wygrales walke na lewym skrzydle!")
        elif kierunek == "prawo":
            print("Brawo! Wygrales walke na prawym skrzydle!")
        print("Z twojego oddzialu pozostalo:")
        a[1] = (a[1] * nasz_wspolczynnik * szczescie) // 1 - b[1]
        b[1] = 0
        print(a)
    else:
        if kierunek == "lewo":
            print("Przegrales na lewym skrzydle!")
        elif kierunek == "prawo":
            print("Przegrales na prawym skrzydle!")
        print("Przeciwnikowi na lewym skrzydle pozostalo:")
        b[1] = b[1] - (a[1] * nasz_wspolczynnik * szczescie) // 1
        a[1] = 0
        print(b)
    time.sleep(3)


def bitwaGlowna():
    budzet = 1000
    zwiady = 0
    armia_przeciwnika = 0
    armia = []
    t = 0

    while t == 0:
        print("Jaki poziom trudnosci wybierasz?")
        print("1: łatwy - armia do pokonania za 600punktow")
        print("2: średni - armia do pokonania za 800punktów")
        print("3: trudny - armia do pokonania za 1000punktów")
        trudnosc = input()
        try:
            trudnosc = int(trudnosc)
            if trudnosc == 1:
                armia_przeciwnika = losowanie_armii(600)
                t = 1
            elif trudnosc == 2:
                armia_przeciwnika = losowanie_armii(800)
                t = 1
            elif trudnosc == 3:
                armia_przeciwnika = losowanie_armii(1000)
                t = 1
            else:
                print("Nie ma podanego poziomu trudnosci")
        except ValueError:
            print("Podałeś inny tryb danych niź liczba")

    x = 1
    while x != 0:
        print("Podaj swoje imie/nick")
        imie = input()
        print("Masz do dyspozycji:", budzet, "złotych monet")

        budzet, zwiady = zwiad(budzet, zwiady, armia_przeciwnika)

        obsadzanie_wojskiem(budzet, armia)

        print("Bitwa!")
        time.sleep(1)

        bitwa("lewo", armia, armia_przeciwnika)
        bitwa("prawo", armia, armia_przeciwnika)

        time.sleep(2)
        print("Finał!")
        print("Walka w centrum")
        print("Nasze sily")
        print(armia)
        print("Sily przeciwnika")
        print(armia_przeciwnika)
        time.sleep(3)
        print(".", end="")
        time.sleep(3)
        print(".", end="")
        time.sleep(3)
        print(".", end="")
        time.sleep(3)

        a = armia_przeciwnika[0]
        b = armia_przeciwnika[1]
        c = armia_przeciwnika[2]
        ich_wartosc_bojowa = b[1]+walka(a, b)*a[1]*1.25+walka(c, b)*c[1]*1.25
        d = armia[0]
        e = armia[1]
        f = armia[2]
        nasza_wartosc_bojowa = e[1]+walka(d, e)*d[1]*1.25+walka(f, e)*f[1]*1.25
        nasz_wspolczynnik = walka(e, b)
        szczescie = random.randint(75, 125) * 0.01
        if nasz_wspolczynnik*nasza_wartosc_bojowa*szczescie > ich_wartosc_bojowa:
            print("Brawo! Wygrales cala bitwe!")
            nasza_wartosc_bojowa = nasz_wspolczynnik*nasza_wartosc_bojowa*szczescie-ich_wartosc_bojowa
            nasza_wartosc_bojowa = nasza_wartosc_bojowa//1
            print("Pozostala wartosc bojowa twojej armii to:")
            print(e[0], nasza_wartosc_bojowa)
            print("Twoj wynik zostanie zapisany w tabeli wynikow")

            wyniki = open('wynikiGraczy.txt', 'a+')
            score = walka(e, ["piechurzy", 0])*nasza_wartosc_bojowa
            wyniki.write('\n')
            wyniki.write(imie+": "+str(score)+" zwiady:"+str(zwiady))
            wyniki.write(',')
            wyniki.close()
            return 0
        else:
            print("Przegrales cala bitwe!")
            ich_wartosc_bojowa = ich_wartosc_bojowa-nasz_wspolczynnik*nasza_wartosc_bojowa*szczescie
            ich_wartosc_bojowa = ich_wartosc_bojowa//1
            print("Pozostala wartosc bojowa armii przeciwnika to:")
            print(b[0], ich_wartosc_bojowa)
            return 0
