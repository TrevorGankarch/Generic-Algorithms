
import random

# Function to create a random individual (chromosome)
def create_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

# Fitness function: Count how many 1's in the individual (maximize this)
def fitness(individual):
    return sum(individual)

# Selection function: Tournament selection
def select(population):
    selected = random.sample(population, 2)
    return max(selected, key=fitness)

# Crossover function: One-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child = parent1[:point] + parent2[point:]
    return child

# Mutation function: Flip a bit with a small probability
def mutate(individual, mutation_rate=0.01):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

# Genetic Algorithm
def genetic_algorithm(population_size, generations, chromosome_length):
    population = [create_individual(chromosome_length) for _ in range(population_size)]

    for gen in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        print(f"Generation {gen}: Best fitness = {fitness(population[0])}")
        
        new_population = population[:2]  # Elitism: keep top 2 individuals
        while len(new_population) < population_size:
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
        
    return population[0]

# Running the Genetic Algorithm
best_individual = genetic_algorithm(population_size=20, generations=100, chromosome_length=10)
print(f"Best individual: {best_individual} with fitness = {fitness(best_individual)}")
