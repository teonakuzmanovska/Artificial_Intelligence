from constraint import *
# [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
# [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
# [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7],
# [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7],
# [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7],
# [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],
# [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7],
# [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]

def my_constraint(q1, q2):
    q1_x = q1[0]
    q1_y = q1[1]
    q2_x = q2[0]
    q2_y = q2[1]
    if q1_x == q2_x or q1_y == q2_y or abs(q1_x - q2_x) == abs(q1_y - q2_y):
        return False
    else:
        return True

if __name__ == '__main__':
    n = int(input())
    problem = Problem(BacktrackingSolver())

    variables = []
    domain = []

    for i in range(n):
        variables.append(i+1)
        for j in range(n):
            domain.append((i, j))

    # for variable in variables:
    #     problem.addVariable(variable, Domain(set(range(100))))

    problem.addVariables(variables, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    for queen1 in variables:
        for queen2 in variables:
            if queen1 != queen2:
                problem.addConstraint(my_constraint, (queen1, queen2))
    # ----------------------------------------------------

    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())

#         from constraint import *
#
# if __name__ == '__main__':
#     problem = Problem(BacktrackingSolver())
#     variables = ["A", "B", "C", "D", "E", "F"]
#     for variable in variables:
#         problem.addVariable(variable, Domain(set(range(100))))
#
#     # ---Tuka dodadete gi ogranichuvanjata----------------
#
#     # ----------------------------------------------------
#
#     print(problem.getSolution())
