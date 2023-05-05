from LMIS_deletion import A
from LMIS_included import Algo
import csv
import ast


class AlgorithmExecutioner:

    def __init__(self, bidding_profile, contribution, demand):
        self.P1 = Algo(bidding_profile, contribution, demand)
        self.P2 = A(bidding_profile, contribution, demand)

    def run(self):
        sol, cost = self.P1.run()
        order, final_sol, final_cos = self.P2.run()
        print("---------- Solution for instance: ", filename, "----------")
        print("LMIS solution is:", sol)
        print("The cost is:", cost)
        print("Order of selection is:", order)
        print("LMIS solution after deletion is:", final_sol)
        print("The final cost after deletion is:", final_cos)


if __name__ == '__main__':
    filenames = ['instance01.csv', 'instance02.csv']
    for filename in filenames:
        with open(filename) as file:
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
