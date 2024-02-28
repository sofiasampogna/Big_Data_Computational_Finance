import numpy as np
from scipy.optimize import linprog

# I generate the vector of coefficients in the objective function 
c = np.array([1,1,1,1,1,1,1])
A = np.zeros((7,7))

# I create a row for each constraint
A[0] = np.array([-1,0,-1,-1,-1,0,-1])
A[1] = np.array([-1,-1,0,-1,-1,-1,0])
A[2] = np.array([0,-1,-1,0,-1,-1,-1])
A[3] = np.array([-1,0,-1,-1,0,-1,-1])
A[4] = np.array([-1,-1,0,-1,-1,0,-1])
A[5] = np.array([-1,-1,-1,0,-1,-1,0])
A[6] = np.array([0,-1,-1,-1,0,-1,-1])
b = np.array([-14, -13, -15, -16, -19, -18, -11])

# It is now time to solve. All variables are constrained to be non-negative, so I don't need to specify the bounds; this is the default
res = linprog(c, A_ub=A, b_ub=b, method='revised simplex', options={"disp": True})

# Print the solution. Recall that the wealth is the last variable. 
res.x