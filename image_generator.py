import random
from time import sleep
import cv2
import numpy as np


class DNA:
    genes = []
    fitness_score = 0

    def __init__(self):
        self.genes = np.array(
            [random.choice([0, 255]) for i in range(11 * 12)]
        )

    def fitness(self):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1

        self.fitness_score = score / len(target)

    def crossover(self, obj):
        child = DNA()
        breakpoint = random.randrange(0, len(target))

        for i in range(len(target)):
            if i > breakpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = obj.genes[i]

        return child

    def mutate(self):
        for i in range(len(target)):
            if random.random() <= mutation_rate:
                self.genes[i] = random.choice([0, 255])

    def get_phrase(self):
        return "".join(self.genes)


population_size = int(input("Population: "))

target = cv2.imread("image.png", 0).reshape(11 * 12)
cv2.imshow("Original image", target.reshape(11, 12))

population = [DNA() for i in range(population_size)]
mutation_rate = 0.0001


# Draw
iterations = 0
while True:
    # sleep(0.00)
    iterations += 1
    for i in population:
        i.fitness()

    # extra
    best = 0
    for i in population:
        if best < i.fitness_score:
            best = i.fitness_score
            phrase = np.array(i.genes.reshape(11, 12), dtype=np.uint8)
    print(
        "Generation:",
        iterations,
        # "  Best match:",
        # phrase,
        "  Score:",
        str(best * 100)[:5],
    )
    cv2.imshow("Generated image", phrase)
    cv2.waitKey(1)

    found = True
    for i in range(11 * 12):
        if not phrase.reshape(11 * 12)[i] == target[i]:
            found = False

    if found:
        cv2.waitKey(0)
        break

    # if phrase.reshape(11 * 12) == target.reshape(11 * 12):
    #     cv2.waitKey(0)
    #     break

    # extra over

    matingPool = []

    for i in range(len(population)):
        n = int(population[i].fitness_score * 100) + 1

        for j in range(n):
            matingPool.append(population[i])

    for i in range(len(population)):
        a = random.randrange(0, len(matingPool))
        b = random.randrange(0, len(matingPool))

        parent_a = matingPool[a]
        parent_b = matingPool[b]

        child = parent_a.crossover(parent_b)
        child.mutate()

        population[i] = child
