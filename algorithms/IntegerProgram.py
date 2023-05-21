from pulp import *


class IP:
    def __init__(self, bidding_profile, contribution, demand):
        self.c = []
        self.intervals = []
        for i in range(len(bidding_profile)):
            self.c.append(bidding_profile[i][0])
            self.intervals.append(bidding_profile[i][1])
        self.q = contribution
        self.d = demand
        self.xi = []

    def solve(self):
        # Create a binary optimization problem
        prob = LpProblem("IntegerProgram", LpMinimize)

        # Create decision variables xi
        self.xi = [LpVariable("x{}".format(i), cat=LpBinary) for i in range(len(self.c))]

        # Define the objective function
        objective = lpSum(self.xi[i] * self.c[i] for i in range(len(self.c)))
        prob += objective

        # Add constraints
        for j in range(len(self.d)):
            constraint_terms = []
            for i in range(len(self.c)):
                if self.intervals[i][0] - 1 <= j <= self.intervals[i][1] - 1:
                    constraint_terms.append(self.xi[i] * self.q[i])
            constraint = lpSum(constraint_terms) >= self.d[j]
            prob += constraint

        # Solve the problem
        prob.solve()

        # Check the status of the solution
        if LpStatus[prob.status] != 'Optimal':
            print("No optimal solution found.")
            return None, None

        # Get the optimal values of xi
        optimal_values = [value(self.xi[i]) for i in range(len(self.c))]

        # Calculate the minimum sum
        min_sum = sum(optimal_values[i] * self.c[i] for i in range(len(self.c)))

        return optimal_values, min_sum
