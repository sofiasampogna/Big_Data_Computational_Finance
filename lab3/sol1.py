c = [-13, -23]
A = [[5, 15], [4, 4], [35, 20]]
b = [480, 160, 1190]
from scipy.optimize import linprog
res = linprog(c, A_ub = A, b_ub=b, bounds = [0, None])
print(res)