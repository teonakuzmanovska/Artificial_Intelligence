from constraint import *


def check_valid(s, e, n, d, m, o, r, y):  # posebna bukva za sekoja promenliva
    # s = 3, e = 2, n = 5, d = 4, send = 3254
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

    return send + more == money


if __name__ == "__main__":
    #  SEND 2819
    #  + MORE + 0368
    #  = MONEY = 03187
    problem = Problem(BacktrackingSolver())

    variables = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))  #  set za da se zemat site vrednosti od 0-9

    problem.addConstraint(AllDifferentConstraint(), variables)  # site 8 promenlivi kje imaat razlichni vrednosti
    problem.addConstraint(check_valid, variables)

    solution = problem.getSolution()
    print(solution)