import random as rd
import string
import time
import matplotlib.pyplot as plt

# the fitness value
def fitness(target, word):
    if len(target) != len(word):
        return 1 + abs(len(target) - len(word)) / max([len(target), len(word)])

    else:
        max_ = 0

        for i in range(len(word)):
            max_ += abs((ord(target[i]) - ord(word[i]))/ 255)

        return max_ / len(word)

# get the word to gess
word = input("The word to gess: ")

# set the charser
charset = string.printable

def new_pop(pop_size, selct_rate, mut_rate):
    # init the population
    pop = []
    pop_nb = 0
    pop_nbs = []
    pop_mean_acuraccys = []
    pop_worst = []
    pop_best = []
    best = ""

    for _ in range(pop_size):
        size = rd.randint(0, 100)
        word_ = ""
        for _ in range(size):
            word_ += rd.choice(charset)
        pop.append(word_)

    # the loop
    while best != word and pop_nb <= 200:
        total_accuracy = 0
        best_fitness = 100000000000000000
        worst_fitness = 0

        for _word in pop:
            total_accuracy += fitness(word, _word)
            if fitness(word, _word) < best_fitness:
                best_fitness = fitness(word, _word)
                best = _word

            if fitness(word, _word) > worst_fitness:
                worst_fitness = fitness(word, _word)


        new_pop = []
        while len(new_pop) // pop_size < selct_rate:
            while True:
                a = rd.choice(pop)
                if fitness(word, a) < rd.random() * total_accuracy / pop_size or rd.random() < .001:
                    break

            while True:
                b = rd.choice(pop)
                if fitness(word, b) < rd.random() * total_accuracy / pop_size or rd.random() < .001:
                    break

            size = (len(a) + len(b)) // 2
            
            new = ""
            for i in range(size):
                if rd.random() < mut_rate:
                    new += rd.choice(charset)
                elif  i < len(a) and i < len(b):
                    new += rd.choice((a[i], b[i]))
                elif i < len(a):
                    new += a[i]
                else:
                    new += b[i]
                

            new_pop.append(new)

        while len(new_pop) != pop_size:
            size = rd.randint(0, 100)
            word_ = ""
            for _ in range(size):
                word_ += rd.choice(charset)
            new_pop.append(word_)

        pop = new_pop
        pop_nb += 1
        pop_nbs.append(pop_nb)
        pop_best.append(best_fitness)
        pop_mean_acuraccys.append( (total_accuracy / pop_size))
        pop_worst.append(worst_fitness)

    print("%s %s %s" %(pop_nb, best, best_fitness))

    return pop_nbs, pop_mean_acuraccys, pop_worst, pop_best


pop_size = 64
selection_rate = 0.85
mutation_rate = 0.01

population = []

# init
for _ in range(pop_size):
    data = rd.randint(0, 1000), rd.random(), rd.random()
    population.append(data)


# run the data
for i in range(200):

    # get the fitness
    better_population = []
    total_fitness = 0
    for data in population:
        beg = time.time()
        a, b, c, d = new_pop(data[0], data[1], data[2])
        new = {}
        new["fitness"] = (len(a) / 201 + d[-1]) / 2 + time.time() - beg
        new["genome"] = data  
        better_population.append(new) 
        total_fitness += new["fitness"]

    # sorte
    better_population = sorted(better_population, key = lambda x : x["fitness"])
    new_population = []

    # selecte the randomly the best
    while len(new_population) / pop_size < selection_rate:

        # select 2 parents
        while True:
            a = rd.choice(better_population)
            if a["fitness"] / total_fitness >= rd.random():
                a = a["genome"]
                break

        while True:
            b = rd.choice(better_population)
            if b["fitness"] / total_fitness <= rd.random():
                b = b["genome"]
                break

        # create the new ellement
        new = [0,0,0]
        for j in range(3):
            new[j] = rd.choice((a[j], b[j]))

        # mutation
        if rd.random() < mutation_rate:
            new[0] += rd.randint(1, 10) * rd.choice([-1, 1])
        if rd.random() < mutation_rate:
            new[1] += rd.random() * rd.choice([-1, 1])
        if rd.random() < mutation_rate:
            new[2] += rd.random() * rd.choice([-1, 1])

        new_population.append(new)

    # the new element
    while len(new_population) != pop_size:
        data = rd.randint(0, 1000), rd.random(), rd.random()
        new_population.append(data)

    # the new pop 
    population = new_population
    print("%s => %s, %s" %(i, better_population[-1]["fitness"], better_population[-1]["genome"]))