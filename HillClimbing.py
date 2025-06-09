from heuristics import heuristic, get_neighbors
import random


def hill_climbing(n):
    current = list(range(n))
    random.shuffle(current)
    current_h = heuristic(current, n, admissible=False)

    while True:
        neighbors = get_neighbors(current, n)
        neighbor_hs = [(heuristic(nei, n, admissible=False), nei) for nei in neighbors]
        best_h = min(h for h, _ in neighbor_hs)

        best_neighbors = [nei for h, nei in neighbor_hs if h == best_h]
        best_neighbor = random.choice(best_neighbors)

        if best_h >= current_h:
            break  # chegou num mínimo local

        current, current_h = best_neighbor, best_h

        if current_h == 0:
            break  # solução ótima

    return current, current_h == 0
