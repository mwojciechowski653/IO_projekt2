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
        return -100
    else:
        return walki(t1, l, t2, s, t3, p)

