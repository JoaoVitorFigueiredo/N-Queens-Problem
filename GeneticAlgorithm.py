import random


def fitness(individual):
    """
    Número de pares de rainhas que não se atacam
    Era legal testar também com o numero de rainhas que estejam mal *-1 pra ficar maximizavel
    """
    n = len(individual)
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):  # Rever se isso faz sentido
                non_attacking += 1
    return non_attacking


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    return parent1[:point] + parent2[point:]


def mutate(individual, mutation_rate=0.03):
    if random.random() < mutation_rate:
        idx = random.randint(0, len(individual) - 1)
        individual[idx] = random.randint(0, len(individual) - 1)
    return individual


def genetic_algorithm(n=8, population_size=1000, generations=500):
    population = [random.choices(range(n), k=n) for _ in range(population_size)]
    max_fitness = (n * (n - 1)) // 2

    for gen in range(generations):
        population = sorted(population, key=lambda x: -fitness(x))
        if fitness(population[0]) == max_fitness:
            print("Melhor individuo")
            return population[0]

        next_generation = population[:10]  # Elitismo mas pode ser outra
        while len(next_generation) < population_size:
            p1, p2 = random.choices(population[:200], k=2)
            child = crossover(p1, p2)
            child = mutate(child)
            next_generation.append(child)
        population = next_generation
    print("Não foi encontrada uma solução\n"
          f"Melhor individuo: {fitness(population[0])}")
    return population[0]
