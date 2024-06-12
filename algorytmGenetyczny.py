import math
import numpy as np
import pygad
import matplotlib.pyplot as plt
from funkcjeRobocze import wczytaniePlikuDoAlgGen
from bitwa import walkaDlaAlgGen

armies = wczytaniePlikuDoAlgGen()

# 1,2 lub 3 - typ jednostki, 0-1 liczebnosc od 0 do 1000
gene_space = [[1, 3], (0, 1), [1, 3], (0, 1), [1, 3], (0, 1)]
moneyBudget = 1000


def walki(t1, l, t2, s, t3, p):
    score = 0
    for army in armies:
        left = walkaDlaAlgGen(t1, army[0]) * l - army[1]
        right = walkaDlaAlgGen(t3, army[4]) * p - army[5]
        if left >= 0:
            score += 100
        else:
            score -= 100

        if right >= 0:
            score += 100
        else:
            score -= 100

        genArmy = [t2, walkaDlaAlgGen(t1, t2) * left * 1.25 + s + walkaDlaAlgGen(t3, t2) * right * 1.25]
        enemyArmy = [army[2], walkaDlaAlgGen(army[0], army[2]) * min(0, left) * 1.25 + army[3] + walkaDlaAlgGen(army[4], army[2]) * min(0, right) * 1.25]

        result = walkaDlaAlgGen(genArmy[0], enemyArmy[0]) * genArmy[1] - enemyArmy[1]
        if result >= 0:
            score += 500 + result
        else:
            score -= 500 + result 

    return score


def fitness_func(model, solution, solution_idx):
    t1, l, t2, s, t3, p = solution
    money = 0
    l = l * 1000 // 1
    s = s * 1000 // 1
    p = p * 1000 // 1
    if t1 == 1:
        money += l
    elif t1 == 2:
        money += l*1.5
    elif t1 == 3:
        money += l*2

    if t2 == 1:
        money += s
    elif t2 == 2:
        money += s*1.5
    elif t2 == 3:
        money += s*2

    if t3 == 1:
        money += p
    elif t3 == 2:
        money += p*1.5
    elif t3 == 3:
        money += p*2

    if money > moneyBudget:
        return -10000
    else:
        return walki(t1, l, t2, s, t3, p)

