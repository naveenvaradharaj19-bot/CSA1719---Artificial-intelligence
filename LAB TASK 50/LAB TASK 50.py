# Genetic Algorithm for Neural Network

import random
import math

random.seed(1)

# Input data for AND gate
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

Y = [0, 0, 0, 1]

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Neural network
def predict(weights, x):

    output = sigmoid(
        weights[0] * x[0] +
        weights[1] * x[1] +
        weights[2]
    )

    return output

# Fitness function
def fitness(weights):

    error = 0

    for i in range(len(X)):

        output = predict(weights, X[i])

        error += (output - Y[i]) ** 2

    return 1 / (1 + error)

# Create population
population = []

for i in range(10):

    chromosome = [
        random.uniform(-5, 5),
        random.uniform(-5, 5),
        random.uniform(-5, 5)
    ]

    population.append(chromosome)

# Genetic algorithm
for generation in range(100):

    population.sort(
        key=fitness,
        reverse=True
    )

    parents = population[:5]

    new_population = parents.copy()

    while len(new_population) < 10:

        p1 = random.choice(parents)
        p2 = random.choice(parents)

        # Crossover
        child = []

        for i in range(3):

            if random.random() < 0.5:
                child.append(p1[i])
            else:
                child.append(p2[i])

        # Mutation
        for i in range(3):

            if random.random() < 0.1:
                child[i] += random.uniform(-1, 1)

        new_population.append(child)

    population = new_population

# Best neural network
best = max(population, key=fitness)

print("Best fitness:", round(fitness(best), 4))

print("Predicted values:")

for x in X:

    output = predict(best, x)

    if output >= 0.5:
        print(1)
    else:
        print(0)
