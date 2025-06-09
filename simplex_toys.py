import pulp as pl

def solve_toy():
    x1 = pl.LpVariable("carros", lowBound=0, cat="Continuous")
    x2 = pl.LpVariable("bonecas", lowBound=0, cat="Continuous")
    x3 = pl.LpVariable("puzzles", lowBound=0, cat="Continuous")

    prob = pl.LpProblem("Brinquedos", pl.LpMaximize)
    prob += 3*x1 + 5*x2 + 4*x3            
    prob += x1 + 2*x2 +     x3 <= 40       
    prob += 2*x1 + 1*x2 + 3*x3 <= 60      
    prob += x1 + 1*x2 + 2*x3 <= 40       

    prob.solve(pl.PULP_CBC_CMD(msg=False))
    print("Status :", pl.LpStatus[prob.status])
    for v in (x1, x2, x3):
        print(f"{v.name:8} = {v.value():>5}")
    print("Profit  =", pl.value(prob.objective))

if __name__ == "__main__":
    solve_toy()
