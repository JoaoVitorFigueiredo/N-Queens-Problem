from GeneticAlgorithm import genetic_algorithm
from AStar import a_star
from HillClimbing import hill_climbing
import time

if __name__ == "__main__":

    board = ""
    n = int(input("n: "))
    alg = int(input("alg [GA,AS,HC]: "))
    solution, success = None, None
    match alg:
        case 1:
            start_time = time.time()
            solution, success = genetic_algorithm(n, int(input("pop_size: ")), int(input("generations: ")))
            end_time = time.time()
            print("Execution Time:" + str(end_time - start_time))

        case 2:
            start_time = time.time()
            solution, success = a_star(n)
            end_time = time.time()
            print("Execution Time:" + str(end_time - start_time))

        case 3:
            start_time = time.time()
            solution, success = hill_climbing(n)
            end_time = time.time()
            print("Execution Time:" + str(end_time - start_time))

    print(solution)
    print(success)

    if solution:
        for i in range(n):
            try:
                queen_position = solution[i]
                board += ("[ ]" * queen_position) + "[x]" + ("[ ]" * (n-queen_position-1)) + "\n"
            except:

                board += ("[ ]" * n) + "\n"

        print(board)

    else:
        print("No solution found")
