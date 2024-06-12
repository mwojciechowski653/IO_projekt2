from funkcjeRobocze import wczytaniePlikuDoAlgGen
from bitwa import walkaDlaAlgGen


def ileWygranych(army):
    t1, l, t2, s, t3, p = army
    money = 0
    if t1 <= 1 / 3:
        t1 = 1
    elif t1 <= 2 / 3:
        t1 = 2
    else:
        t1 = 3

    if t2 <= 1 / 3:
        t2 = 1
    elif t2 <= 2 / 3:
        t2 = 2
    else:
        t2 = 3

    if t3 <= 1 / 3:
        t3 = 1
    elif t3 <= 2 / 3:
        t3 = 2
    else:
        t3 = 3

    # print(t1, t2, t3)
    l = l * 1000 // 1
    s = s * 1000 // 1
    p = p * 1000 // 1
    if t1 == 1:
        money += l
    elif t1 == 2:
        money += l * 1.5
    elif t1 == 3:
        money += l * 2

    if t2 == 1:
        money += s
    elif t2 == 2:
        money += s * 1.5
    elif t2 == 3:
        money += s * 2

    if t3 == 1:
        money += p
    elif t3 == 2:
        money += p * 1.5
    elif t3 == 3:
        money += p * 2

    print("Wykorzystany budżet:", money)
    score = 0
    winningLeft = 0
    winningRight = 0
    armies = wczytaniePlikuDoAlgGen()
    for army in armies:
        left = walkaDlaAlgGen(t1, army[0]) * l - army[1]
        right = walkaDlaAlgGen(t3, army[4]) * p - army[5]
        if left >= 0:
            winningLeft += 1

        if right >= 0:
            winningRight += 1

        genArmy = [t2, walkaDlaAlgGen(t1, t2) * left * 1.25 + s + walkaDlaAlgGen(t3, t2) * right * 1.25]
        enemyArmy = [army[2], walkaDlaAlgGen(army[0], army[2]) * min(0, left) * 1.25 + army[3] + walkaDlaAlgGen(army[4], army[2]) * min(0, right) * 1.25]

        result = walkaDlaAlgGen(genArmy[0], enemyArmy[0]) * genArmy[1] - enemyArmy[1]
        if result >= 0:
            score += 1

    print("Na", len(armies), "bitw")
    print("Lewe skrzydło wygralo:", winningLeft, str(winningLeft/len(armies)*100)+"%")
    print("Prawe skrzydło wygralo:", winningRight, str(winningRight/len(armies)*100)+"%")
    print("Cala bitwa zostala wygrana:", score, str(score/len(armies)*100)+"%")