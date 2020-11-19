import random
import cv2
import numpy as np

# genes_length = 5  # number of cities
# population_count = 1000  # number of salesmen
mutation_rate = 0.005

genes_length = int(input("Number of cities: "))
population_count = int(input("Population: "))

map_range = 500  # 500x500 grid for different locations


cities = [
    [random.randrange(0, map_range), random.randrange(0, map_range)] for i in range(genes_length)
]


class SalesMan:
    genes = []  # order of visiting cities
    fitness = 0
    distances = 0

    def __init__(self):
        self.genes = [i for i in range(genes_length)]
        random.shuffle(self.genes)

    def calculate_fitness(self):
        distance = 0
        current_position = cities[self.genes[0]]
        for i in range(1, genes_length):
            distance += (
                (current_position[0] - cities[self.genes[i]][0]) ** 2
                + (current_position[1] - cities[self.genes[i]][1]) ** 2
            ) ** 0.5
            current_position = cities[self.genes[i]]
        self.distances = distance
        self.fitness = (
            10000 / distance
        )  # we want fitness to be grater than 1 and also we want to have different fitness values for different distances


# Generating the initial population
population = []
for i in range(population_count):
    population.append(SalesMan())


generation_count = 0
while True:
    generation_count += 1
    # Calculating the fitness
    for i in population:
        i.calculate_fitness()

    # Finding best fitness value
    best_fitness = 0
    best_individual = population[0]
    for i in population:
        if i.fitness > best_fitness:
            best_fitness = i.fitness
            best_individual = i

    print(f"Generation: {generation_count}, Total distance: {best_individual.distances}")

    # Draw best individual
    order = best_individual.genes
    image = np.ones((map_range, map_range))

    pts = np.array([cities[i] for i in order], dtype=np.int32)
    for pt in pts:
        image = cv2.circle(image, (pt[0], pt[1]), 5, (0, 255, 0), 2)

    pts = pts.reshape((-1, 1, 2))
    image = cv2.polylines(image, [pts], False, (0, 255, 0), 2)
    cv2.imshow("Map", image)
    cv2.waitKey(1)

    # If the target is found, then break
    # if best_fitness == 1.0:
    # break

    # Generating a mating pool
    mating_pool = []
    for i in population:
        for j in range(int(i.fitness) ** 3):
            mating_pool.append(i)

    population = []

    # Generating the next generation
    for i in range(population_count):
        # Selection
        parent_A = random.choice(mating_pool)
        parent_B = random.choice(mating_pool)

        # Crossover
        break_point_0 = random.randrange(0, genes_length)
        break_point_1 = random.randrange(break_point_0, genes_length)
        child = SalesMan()
        child.genes = [-1 for i in range(genes_length)]
        child.genes[break_point_0:break_point_1] = parent_A.genes[break_point_0:break_point_1]
        for i in parent_B.genes:
            if i not in child.genes:
                for j in range(genes_length):
                    if child.genes[j] == -1:
                        child.genes[j] = i
                        break

        # Mutation
        record = random.random()
        if record < mutation_rate:
            break_point = random.randrange(0, genes_length)
            child.genes[break_point], child.genes[(break_point + 1) % genes_length] = (
                child.genes[(break_point + 1) % genes_length],
                child.genes[break_point],
            )

        # Add child into the new population
        population.append(child)
        # print(child.genes)
