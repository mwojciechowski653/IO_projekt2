import math
import numpy as np
import pygad
import matplotlib.pyplot as plt
from funkcjeRobocze import wczytaniePlikuDoAlgGen
from bitwa import walkaDlaAlgGen

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
            score -= 500

        if right >= 0:
            score += 100
        else:
            score -= 500

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
    if t1 / 3 <= 1/3:
        t1 = 1
    elif t1 / 3 <= 2/3:
        t1 = 2
    else:
        t1 = 3

    if t2 / 3 <= 1/3:
        t2 = 1
    elif t2 / 3 <= 2/3:
        t2 = 2
    else:
        t2 = 3

    if t3 / 3 <= 1/3:
        t3 = 1
    elif t3 / 3 <= 2/3:
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


num_generations = 100
num_parents_mating = 4
keep_parents = 2
mutation_percent_genes = 18
sol_per_pop = 10
num_genes = 6

initial_population = np.random.rand(sol_per_pop, num_genes)

parent_selection_type = "rws"

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_type=float,
                       gene_space=gene_space,
                       keep_parents=keep_parents,
                       parent_selection_type=parent_selection_type,
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
plt.yscale("log", base=10)
plt.savefig("wykres.png")

# Parameters of the best solution :  [1.         0.04210015 1.         0.4163792  1.         0.51083522]
# Fitness value of the best solution = 2636793.375
