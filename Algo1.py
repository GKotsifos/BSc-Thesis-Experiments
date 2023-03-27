from LMIS import *


class A:

    def __init__(self, bidding_profile, contribution, demand):
        """
        Constructor
        :param bidding_profile: b / = (c, I) - [c , [s, f]] // size n
        :param contribution: q / == r   // size n
        :param demand: d / size m
        """

        self.b_profile = bidding_profile
        self.contribution = contribution
        self.demand = demand

    def calc_Q(self, q):

        sum_q = [0] * len(self.demand)
        for j in range(1, len(self.demand) + 1):
            for x in range(len(b)):
                if b[x][1][0] <= j <= b[x][1][1]:
                    sum_q[j - 1] += q[x]
        return sum_q

    def run(self):

        Q = self.calc_Q(self.contribution)
        p = [0] * len(self.b_profile)
        T = [0] * len(self.b_profile)
        for i in range(len(self.b_profile)):
            p[i] = self.b_profile[i][0]
            T[i] = self.b_profile[i][1]

        r = self.contribution
        D = [0] * len(self.demand)
        for i in range(len(Q)):
            D[i] = Q[i] - self.demand[i]

        J = []
        for i in range(1, len(q)+1):
            J.append(i)

        m = len(self.demand)

        P2 = LMIS(p, T, r, D, J, m)
        alg2_sol, alg2_cost = P2.run()

        return alg2_sol, alg2_cost


# --------Example---------
b = [[10, [1, 3]], [2, [2, 4]], [3, [1, 5]]]
q = [2, 1, 4]
d = [2, 3, 4, 1, 4]
P1 = A(b, q, d)
sol, cost = P1.run()
print("LMIS solution is:", sol)
print("The cost is:", cost)
