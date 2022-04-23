from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = []
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))


    def my_constraint(variables):
        i = 0
        kocka = 0
        my_dict = {}
        for var in variables:
            while i < 9:
                my_dict[kocka] = var
                i += 1
            kocka += 1
        for cube in my_dict:


    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(my_constraint, variables)

    # ----------------------------------------------------

    print(problem.getSolution())