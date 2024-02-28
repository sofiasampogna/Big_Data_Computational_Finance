import numpy as np
from gurobipy import *
from gurobipy import GRB

# Declare and initialize model
m = Model('Task 7')

# Add variables
x = m.addMVar(shape=22, vtype=GRB.CONTINUOUS, name="x")

# Create matrix A
A = np.zeros((8,22))

# I create a row for each constraint
A[0] = np.concatenate([[1,1,1,-1],np.zeros(18)])
A[1] = np.concatenate([[-0.01, -0.018, -1.025, 1.005, 1, 1, -1],np.zeros(15)])
A[2] = np.concatenate([[-0.01, -1.018, 0, 0, -0.018, -1.025, 1.005, 1, 1, -1],np.zeros(12)])
A[3] = np.concatenate([[-0.01, 0, 0, 0, -1.018, 0, 0, -0.018, -1.025, 1.005, 1, 1, -1],np.zeros(9)])
A[4] = np.concatenate([[-0.01], np.zeros(6), [-1.018, 0, 0, -0.018, -1.025, 1.005, 1, 1, -1],np.zeros(6)])
A[5] = np.concatenate([[-0.01], np.zeros(9), [-1.018, 0, 0, -0.018, -1.025, 1.005, 1, 1, -1],np.zeros(3)])
A[6] = np.concatenate([[-0.01], np.zeros(12), [-1.018, 0, 0, -0.018, -1.025, 1.005, 1, -1, 0]])
A[7] = np.concatenate([[-1.01], np.zeros(15), [-1.018, 0, 0, -1.025, 1.005, -1]])

# The right-hand-side constants
rhs = np.array([100, 500, 100, -600, -500, 200, 600, -900])

# Adding the constraints
m.addConstr(A @ x == rhs, name="c")

# Setting the objective function. Here, I can be flexible and define a maximization problem, unlike in linprog
obj = np.concatenate([[0]*21,[1]])
m.setObjective(obj @ x, GRB.MAXIMIZE)

m.optimize()
print(x.X)