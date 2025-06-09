
def heuristic(state):
    """Heurística: número de ataques diagonais se continuarmos com esse estado"""
    """Tanto diretamente, quanto indiretamente"""
    """Retirado parcialmente de: https://www.cs.miami.edu/home/visser/csc329-files/InformedSearchHeuristics.pdf"""
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts  # não penaliza estados incompletos

def get_neighbors(state, n):
    """Gera vizinhos trocando duas rainhas de lugar"""
    neighbors = []
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = state.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors
