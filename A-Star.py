import heapq


def is_safe(partial_state, row):
    """Verifica se a rainha pode ser colocada na próxima coluna, na linha `row`"""
    col = len(partial_state)
    for c, r in enumerate(partial_state):
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True


def heuristic(state, n, admissible=True):
    if admissible:
        return admissible_heuristic(state)
    else:
        return non_admissible_heuristic(state, n)


def non_admissible_heuristic(state, n):
    """Heurística: número estimado de ataques diagonais se continuarmos com esse estado"""
    """Tanto diretamente, quanto indiretamente"""
    """Retirado parcialemente de: https://www.cs.miami.edu/home/visser/csc329-files/InformedSearchHeuristics.pdf"""
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts + (n - len(state))  # penaliza estados incompletos


def admissible_heuristic(state):
    """Heurística: número de ataques diagonais se continuarmos com esse estado"""
    """Tanto diretamente, quanto indiretamente"""
    """Retirado parcialmente de: https://www.cs.miami.edu/home/visser/csc329-files/InformedSearchHeuristics.pdf"""
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts  # não penaliza estados incompletos


def a_star_n_queens(n):
    """Resolve o problema das N-rainhas usando A*"""
    heap = []
    heapq.heappush(heap, (0, [], 0))  # (f_score, state, g_score)

    while heap:
        f, state, g = heapq.heappop(heap)

        if len(state) == n:
            return state  # Solução encontrada

        for row in range(n):
            if is_safe(state, row):
                new_state = state + [row]
                g_new = g + 1
                h = heuristic(new_state, n)
                f_new = g_new + h
                heapq.heappush(heap, (f_new, new_state, g_new))

    return None  # Nenhuma solução encontrada


# Exemplo de uso
if __name__ == "__main__":
    n = 8
    solution = a_star_n_queens(n)
    if solution:
        print(f"Solução encontrada para {n} rainhas:")
        for col, row in enumerate(solution):
            print(f"Coluna {col}, Linha {row}")
    else:
        print("Nenhuma solução encontrada.")
