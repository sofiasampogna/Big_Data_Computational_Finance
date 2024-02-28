import numpy as np
from scipy.optimize import linprog

# I generate the vector of coefficients in the objective function and initialize the matrix of contraint coefficients
c = np.concatenate([np.zeros(21), [-1]]) # Recall that linprog has a minimization objective, so we minimize -wealth
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

b = [100, 500, 100, -600, -500, 200, 600, -900]

# It is now time to solve. All variables are constrained to be non-negative, so I don't need to specify the bounds; this is the default
res = linprog(c, A_eq=A, b_eq=b, method='revised simplex', options={"disp": True})

# Print the solution. Recall that the wealth is the last variable. 
res.x