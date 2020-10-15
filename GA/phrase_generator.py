import random
from time import sleep


class DNA:
    genes = []
    fitness_score = 0

    def __init__(self):
        self.genes = [
            chr(random.randrange(32, 128)) for i in range(len(target))
        ]

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
                self.genes[i] = chr(random.randrange(32, 128))

    def get_phrase(self):
        return "".join(self.genes)


target = input("Target phrase: ")
population_size = int(input("Population: "))
population = [DNA() for i in range(population_size)]
mutation_rate = 0.001


iterations = 0
while True:
    iterations += 1
    for i in population:
        i.fitness()

    best = 0
    for i in population:
        if best < i.fitness_score:
            best = i.fitness_score
            phrase = i.get_phrase()
    print(
        "Generation:",
        iterations,
        "  Best match:",
        phrase,
        "  Score:",
        str(best * 100)[:5],
    )
    if phrase == target:
        break

    matingPool = []

    for i in range(len(population)):
        n = int(population[i].fitness_score * 100)

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
