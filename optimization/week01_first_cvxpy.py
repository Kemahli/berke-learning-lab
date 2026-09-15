import cvxpy as cp

x = cp.Variable()
y = cp.Variable()

objective = cp.Minimize(2 * x + 3 * y)

constraints = [
    x + y >= 10,
    x >= 0,
    y >= 0
]

problem = cp.Problem(objective, constraints)
problem.solve()

print("Status:", problem.status)
print("Optimal value:", problem.value)
print("x:", x.value)
print("y:", y.value)
