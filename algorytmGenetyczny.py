import math
import numpy as np
import pygad
import matplotlib.pyplot as plt
from funkcjeRobocze import wczytaniePlikuDoAlgGen
from bitwa import walkaDlaAlgGen
from ileWygranych import ileWygranych

armies = wczytaniePlikuDoAlgGen()

# 0-1 - typ jednostki 1/3 dla każdego typu, 0-1 liczebność od 0 do 1000
gene_space = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
moneyBudget = 1000


def walki(t1, l, t2, s, t3, p):
    score = 0
    for army in armies:
        left = walkaDlaAlgGen(t1, army[0]) * l - army[1]
        right = walkaDlaAlgGen(t3, army[4]) * p - army[5]
        if left >= 0:
            score += 100
        else:
            score -= 200

        if right >= 0:
            score += 100
        else:
            score -= 200

        genArmy = [t2, walkaDlaAlgGen(t1, t2) * left * 1.25 + s + walkaDlaAlgGen(t3, t2) * right * 1.25]
        enemyArmy = [army[2], walkaDlaAlgGen(army[0], army[2]) * min(0, left) * 1.25 + army[3] + walkaDlaAlgGen(army[4], army[2]) * min(0, right) * 1.25]

        result = walkaDlaAlgGen(genArmy[0], enemyArmy[0]) * genArmy[1] - enemyArmy[1]
        if result >= 0:
            score += 500 + result//5
        else:
            score -= 500 + result//5

    return score


def fitness_func(model, solution, solution_idx):
    t1, l, t2, s, t3, p = solution
    money = 0
    if t1 <= 1/3:
        t1 = 1
    elif t1 <= 2/3:
        t1 = 2
    else:
        t1 = 3

    if t2 <= 1/3:
        t2 = 1
    elif t2 <= 2/3:
        t2 = 2
    else:
        t2 = 3

    if t3 <= 1/3:
        t3 = 1
    elif t3 <= 2/3:
        t3 = 2
    else:
        t3 = 3

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
        return -100000
    else:
        return walki(t1, l, t2, s, t3, p)


num_generations = 20
num_parents_mating = 8
keep_parents = 2
mutation_percent_genes = 18
sol_per_pop = 20
num_genes = 6

initial_population = np.random.rand(sol_per_pop, num_genes)

parent_selection_type = "sss"
crossover_type = "two_points"

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_type=float,
                       gene_space=gene_space,
                       keep_parents=keep_parents,
                       parent_selection_type=parent_selection_type,
                       crossover_type=crossover_type,
                       initial_population=initial_population,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : ", solution)
print("Fitness value of the best solution =", solution_fitness)

fitness_values = ga_instance.best_solutions_fitness
plt.plot(fitness_values)
plt.xlabel('Generacja')
plt.ylabel('Fitness')
plt.grid()
plt.savefig("./wykresy/wykres.png")

ileWygranych(solution)

# NAJLEPSZE
# ileWygranych((0.5, 0.406, 1, 0, 0, 0.391))
# [0.5 0.406 1. 0. 0. 0.391]
# Wykorzystany budżet: 1000.0
# Na 5000 bitw
# Lewe skrzydło wygralo: 4728 94.56%
# Prawe skrzydło wygralo: 4505 90.10000000000001%
# Cala bitwa zostala wygrana: 5000 100.0%

# Najlepsze rozwiązanie z WYKRES 1
# Parameters of the best solution :  [1.         0.14637148 1.         0.16492514 0.52171113 0.22048858]
# Fitness value of the best solution = 3107069.0
# Wykorzystany budżet: 950.0
# Na 5000 bitw
# Lewe skrzydło wygralo: 1810 36.199999999999996%
# Prawe skrzydło wygralo: 4784 95.67999999999999%
# Cala bitwa zostala wygrana: 4990 99.8%

# Najlepsze rozwiązania z WYKRES 2
# Parameters of the best solution :  [0.         0.0492478  0.66010416 0.36915246 1.         0.19456259]
# Fitness value of the best solution = 2604570.0
# Wykorzystany budżet: 990.5
# Na 5000 bitw
# Lewe skrzydło wygralo: 304 6.08%
# Prawe skrzydło wygralo: 4320 86.4%
# Cala bitwa zostala wygrana: 5000 100.0%

# Parameters of the best solution :  [1.         0.52462255 0.         0.24863714 1.         0.22385171]
# Fitness value of the best solution = 2350902.0
# Wykorzystany budżet: 995.0
# Na 5000 bitw
# Lewe skrzydło wygralo: 3430 68.60000000000001%
# Prawe skrzydło wygralo: 3634 72.68%
# Cala bitwa zostala wygrana: 4495 89.9%

# Parameters of the best solution :  [1.         0.23257955 1.         0.48890591 0.         0.26936933]
# Fitness value of the best solution = 2294760.0
# Wykorzystany budżet: 989.0
# Na 5000 bitw
# Lewe skrzydło wygralo: 1518 30.36%
# Prawe skrzydło wygralo: 3973 79.46%
# Cala bitwa zostala wygrana: 4781 95.62%
