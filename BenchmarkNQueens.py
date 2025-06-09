import time
import csv

from GeneticAlgorithm import genetic_algorithm
from AStar import a_star
from HillClimbing import hill_climbing
from heuristics import heuristic

def run_algorithms(n, num_runs=10, pop_size=100, generations=500):
    results = []

    for alg_name, alg_func in [
        ("GeneticAlgorithm", lambda: genetic_algorithm(n))
    ]:
        n_runs = num_runs
        if alg_name is "A-star":
            n_runs = 1
        for run in range(n_runs):
            start = time.time()
            solution, solved = alg_func()
            end = time.time()
            duration = end - start



            results.append({
                "Algorithm": alg_name,
                "Run": run + 1,
                "Solved": solved,
                "Time": round(duration, 4),
                "Solution": solution
            })
            print(f"{alg_name} - Run {run + 1}: {'Solved' if solved else 'Not solved'} in {duration:.4f} seconds")


    # Save to CSV
    filename = f"nqueens_results_n{n}_only_HC_AS.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Algorithm", "Run", "Solved", "Time", "Solution"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {filename}")


if __name__ == "__main__":
    for n in [4,5,6,7,8,10,20,50,75,100]:
        run_algorithms(n)
