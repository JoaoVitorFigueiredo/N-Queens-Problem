import heapq
import random
from heuristics import heuristic, get_neighbors



def a_star(n):
    """Resolve o problema das N-rainhas com A* e vizinhança por swap"""
    initial_state = list(range(n))
    random.shuffle(initial_state)
    g = 0
    h = heuristic(initial_state, n)
    f = g + h

    heap = []
    heapq.heappush(heap, (f, initial_state, g))

    visited = set()

    while heap:
        f, state, g = heapq.heappop(heap)
        state_tuple = tuple(state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        h = heuristic(state, n)
        if h == 0:
            return state, True  # Solução encontrada

        for neighbor in get_neighbors(state, n):
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple in visited:
                continue

            g_new = g + 1
            h_new = heuristic(neighbor, n)
            f_new = g_new + h_new
            heapq.heappush(heap, (f_new, neighbor, g_new))

    return None, False  # Nenhuma solução encontrada
