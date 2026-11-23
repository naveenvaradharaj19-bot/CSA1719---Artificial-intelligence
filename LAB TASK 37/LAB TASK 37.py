# Genetic Algorithm

import random

random.seed(1)

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [3, 8, 12, 18, 25, 31]

for generation in range(10):

    # Select best individuals
    population.sort(key=fitness, reverse=True)

    parents = population[:3]

    new_population = parents.copy()

    while len(new_population) < 6:

        p1 = random.choice(parents)
        p2 = random.choice(parents)

        # Crossover
        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.1:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

# Find best solution
best = max(population, key=fitness)

print("Best value:", best)
print("Maximum fitness:", fitness(best))
