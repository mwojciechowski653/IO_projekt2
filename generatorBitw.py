from bitwa import losowanie_armii, walka


def bitwy(ilosc):
    wynikiDoZapisu = []
    for i in range(ilosc):
        armia1 = losowanie_armii(700)
        armia2 = losowanie_armii(1000)
        doZapisu = [armia1[0][0], armia1[0][1], armia1[1][0], armia1[1][1], armia1[2][0], armia1[2][1], armia2[0][0], armia2[0][1], armia2[1][0], armia2[1][1], armia2[2][0], armia2[2][1]]

        wspolczynnik = walka(armia1[0], armia2[0])
        if armia1[0][1] * wspolczynnik > armia2[0][1]:
            armia1[0][1] = (armia1[0][1] * wspolczynnik) // 1 - armia2[0][1]
            armia2[0][1] = 0
        else:
            armia2[0][1] = armia2[0][1] - (armia1[0][1] * wspolczynnik) // 1
            armia1[0][1] = 0

        wspolczynnik = walka(armia1[2], armia2[2])
        if armia1[2][1] * wspolczynnik > armia2[2][1]:
            armia1[2][1] = (armia1[2][1] * wspolczynnik) // 1 - armia2[2][1]
            armia2[2][1] = 0
        else:
            armia2[2][1] = armia2[2][1] - (armia1[2][1] * wspolczynnik) // 1
            armia1[2][1] = 0

        a = armia2[0]
        b = armia2[1]
        c = armia2[2]
        wartoscBojowa2 = b[1] + walka(a, b) * a[1] * 1.25 + walka(c, b) * c[1] * 1.25
        d = armia1[0]
        e = armia1[1]
        f = armia1[2]
        wartoscBojowa1 = e[1] + walka(d, e) * d[1] * 1.25 + walka(f, e) * f[1] * 1.25
        wspolczynnik = walka(e, b)
        if wspolczynnik * wartoscBojowa1 > wartoscBojowa2:
            wartoscBojowa1 = wspolczynnik * wartoscBojowa1 - wartoscBojowa2
            wartoscBojowa1 = wartoscBojowa1 // 1
            win = 1
        else:
            win = 0
        wynikiDoZapisu.append(str(doZapisu[0]) + "," + str(doZapisu[1]) + "," + str(doZapisu[2]) + "," + str(doZapisu[3]) + "," + str(doZapisu[4]) + "," + str(doZapisu[5]) + "," + str(doZapisu[6]) + "," + str(doZapisu[7]) + "," + str(doZapisu[8]) + "," + str(doZapisu[9]) + "," + str(doZapisu[10]) + "," + str(doZapisu[11]) + "," + str(win))
    wyniki = open('rozgrywki.txt', 'a+')
    for wynik in wynikiDoZapisu:
        wyniki.write("\n")
        wyniki.write(wynik)
    wyniki.close()

    print("Dodano:", ilosc, "rekordkow")
