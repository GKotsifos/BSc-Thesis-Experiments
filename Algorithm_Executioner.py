from algorithms.LMIS_deletion import A
from algorithms.LMIS_included import Algo
from algorithms.IntegerProgram import IP
import csv
import ast
import os


class AlgorithmExecutioner:

    def __init__(self, bidding_profile, contribution, demand):
        self.P1 = Algo(bidding_profile, contribution, demand)
        self.P2 = A(bidding_profile, contribution, demand)
        self.P3 = IP(bidding_profile, contribution, demand)

    def run(self):
        sol, cost = self.P1.run()
        order, final_sol, final_cos = self.P2.run()
        opt_values, opt_cost = self.P3.solve()
        print("---------- Solution for instance: ", filename, "----------")
        if sol != 0 and cost != 0:
            print("LMIS solution is:", sol)
            print("The cost is:", cost)
            print("Order of selection is:", order)
            print("LMIS solution after deletion is:", final_sol)
            print("The final cost after deletion is:", final_cos)
        else:
            print("Infeasible Solution for this instance")

        for i in range(len(opt_values)):
            if opt_values[i] > 0:
                opt_values[i] = i + 1

        opt_values = [i for i in opt_values if i != 0]

        if opt_values is not None and opt_cost is not None:
            print("Optimal selection is:", opt_values)
            print("Optimal cost:", opt_cost)


if __name__ == '__main__':
    filenames = ['instance01.csv']
    for filename in filenames:
        dataset_path = os.path.join(os.path.dirname(__file__), 'datasets\\5_workers_5_tasks', filename)
        with open(dataset_path) as file:
            reader = csv.DictReader(file)
            b = []
            q = []
            d = []

            for row in reader:
                if row['bidding_profile'] != '':
                    b.append(ast.literal_eval(row['bidding_profile']))
            file.seek(0)  # reset file pointer
            next(reader)

            for row in reader:
                if row['contribution'] != '':
                    q.append(int(row['contribution']))
            file.seek(0)  # reset file pointer
            next(reader)

            for row in reader:
                if row['demand'] != '':
                    d.append(int(row['demand']))

        main_program = AlgorithmExecutioner(b, q, d)
        main_program.run()
