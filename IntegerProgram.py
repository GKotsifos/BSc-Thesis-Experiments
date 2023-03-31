import cvxpy
import numpy as np

##############################################
# The data for solving the Integer Problem
# c is cost of including a worker / size n
# q is the contribution of a worker / size n
# b is the interval / size n

c = np.array([10, 2, 3])
q = np.array([2, 1, 3])
d = np.array([2, 3, 4, 1, 4])
b = np.array([[1, 3], [1, 5], [1, 5]])

# The variable we are solving for / xi

selection = cvxpy.Variable(len(q), boolean=True)  # qi alla se ti megethos

# Contribution constraint - the sum of contributions should be more than the demand
# for a specific task

contribution_constraint = q @ selection >= d

# Our total utility is the sum of the item utilities
total_cost = c @ selection

# We tell cvxpy that we want to minimize total cost
# subject to contribution_constraint. All constraints in
# cvxpy must be passed as a list

constraints = [contribution_constraint]
cmic = cvxpy.Problem(cvxpy.Minimize(total_cost), constraints=constraints)

# Solving the problem
cmic.solve(solver=cvxpy.GLPK_MI)

print(selection.value)
