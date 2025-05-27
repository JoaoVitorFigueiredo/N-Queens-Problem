from GeneticAlgorithm import genetic_algorithm

if __name__ == "__main__":
    board = ""
    n = int(input("n: "))
    solution = genetic_algorithm(n, int(input("pop_size: ")), int(input("generations: ")))
    print(solution)
    for i in range(n):
        queen_position = solution[i]
        board += ("[ ]" * queen_position) + "[x]" + ("[ ]" * (n-queen_position-1)) + "\n"

    print(board)
