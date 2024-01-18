max_attacking = 8  # Assuming the maximum number of attacking queens is 8

def fitness(c):  # c is the chromosome
    n = len(c)  # n represents the number of queens
    current_attacking = 0

    # Code here to compute the number current_attacking queens

    for i in range(n):
        for j in range(i + 1, n):
            if (c[i] == c[j]) or (abs(c[i] - c[j]) == j - i):
                current_attacking += 1

    f = max_attacking - current_attacking
    return f

# Testing The fitness function.
c = [0, 3, 0, 1]
# c = [3, 1, 7, 5, 8, 2, 4, 6]
print('The number of non-attacking queens', fitness(c))

# initial population generation

import random as rnd

for x in range(5):
    print(rnd.randint(1, 5))

def inital_population(p_size, chromosome_length, gene_min, gene_max):
    p = []  # initialize the population
    for i in range(p_size):
        c = []
        for j in range(chromosome_length):
            c.append(rnd.randint(gene_min, gene_max))
        p.append(c)
    return p

# testing inital_population
p = inital_population(5, 4, 0, 3)
print(p)
# For the given setup the output should be of the following form
#[[2, 3, 3, 0], [1, 2, 0, 2], [2, 1, 3, 2], [3, 1, 0, 3], [2, 1, 1, 0]]

p_f = []  # population with fitness
for c in p:
    p_f.append([fitness(c), c])

# Replace the old population p with P_f
p = p_f
print(p)

# selectionnnn


def selection(p):
    sum_fitness = 0
    pf = []  # percent fitness
    for c in p:
        sum_fitness += c[0]

    cpf = 0  # cummolative fitness
    rn = rnd.randint(0, 99)  # Generate a random number between 0 and 100

    for c in p:
        cpf += (c[0] * 100) / sum_fitness
        if rn <= cpf:
            return c[1]
    return p[rnd.randint(0, len(p) - 1)]

print(selection(p))

# crossover


def crossover(x, y):
    # find the spliting point sp: randomly generate a nuumber between 1 and chromosome_length-2

    sp = rnd.randint(1, len(x) - 2)

    nx = []  # new child 1
    ny = []  # new child 2
    nx = x[:sp] + y[sp:]
    ny = y[:sp] + x[sp:]
    return (nx, ny)

print(p[1][1])
print(p[2][1])
x, y = crossover(p[1][1], p[2][1])
print(x, y)

from random import random

print(random())

# mutation


def mutation(x, mp, gene_min, gene_max):
    rn = rnd.random()  # generate a random number [0,1]
    if rn <= mp:
        loc = rnd.randint(0, len(x) - 1)  # gene to be mutated
        x[loc] = rnd.randint(gene_min, gene_max)
    return x

gene_min = 1
gene_max = 4
mp = 0.9
print(mutation(p[1][1], mp, gene_min, gene_max))


# genetic alogrithm



def GA(p_size, ch_length, gene_min, gene_max, mp, epochs, stopping_condtion):
    # The arguments p_size, ch_length, gene_min, gene_max, mp, represents the
    # population size, chromosome length, minimum value of gene, maximum value of gene,
    # mutation probability, the maximum number of epochs, respectively

    # Generate the initial population
    p = inital_population(p_size, ch_length, gene_min, gene_max)

    stop = 0  # This is the stopping criteria
    gen = 1

    while (gen < epochs):
        pp = p  # The previous population
        np = []  # Initialize the new population

        # Generate new chromosomes by selection, crossover, and mutation
        for i in range(p_size):
            x = selection(p)  # Select a parent chromosome
            y = selection(p)  # Select another parent chromosome

            # Perform crossover to generate two new offspring
            child1, child2 = crossover(x, y)

            # Apply mutation to each offspring with a probability of mp
            child1 = mutation(child1, mp, gene_min, gene_max)
            child2 = mutation(child2, mp, gene_min, gene_max)

            np.append(child1)  # Add the offspring to the new population
            np.append(child2)  # Add the other offspring to the new population

        # Replace the old population with the new population
        p = np

        # Compute the fitness of the current population
        pf = []
        for c in p:
            pf.append([fitness(c), c])
        p = pf

        # Sort the current population and the previous population based on fitness
        pp.sort()
        p.sort()

        # Perform elitism by keeping the best chromosome from the previous population
        p[0] = pp[p_size - 1]

        # Check for stopping conditions
        if pp[p_size - 1][0] == p[p_size - 1][0]:
            stop += 1
        else:
            stop = 0

        if stop == stopping_condtion or p[p_size - 1][0] == 28:
            return p[p_size - 1]

        gen += 1

    return p[p_size - 1]

p_size=20
ch_length=8
gene_min=1
gene_max=8
mp=0.02

epochs=10000000
stoping_condtion=3

solution=GA(p_size,ch_length,gene_min,gene_max,mp,epochs,stoping_condtion)

print("The solution is", solution)