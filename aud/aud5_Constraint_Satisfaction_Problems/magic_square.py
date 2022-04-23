from constraint import *
# 0   1   2   3 | row = 0 ro1+0, row+1, +2,+3
# 4   5   6   7 | row = 1 4+0, 4+1, 4+2 row+4
# 8   9  10  11
# 12  13 14  15
if __name__ == "__main__":
    problem = Problem()

    variables = range(16)
    domain = range(1, 17)

    problem.addVariables(variables, domain)

    problem.addConstraint(AllDifferentConstraint(), variables) #site promenlivi vo vtoriot argument da bidat razlichni

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(4)])

    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34), [col +4 * i for i in range(4)])

    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

    solution = problem.getSolution()

    print(solution)