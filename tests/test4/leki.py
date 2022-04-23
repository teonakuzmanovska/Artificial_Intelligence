from constraint import *
if __name__ == '__main__':

    solver = input()
    if solver == "BackTrackingSolver":
        problem = Problem(BacktrackingSolver())
    if solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    if solver == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())

    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    variables = range(81)

    kocki = []
    for i in range(0, 55, 27):
        for j in range(i, i + 7, 3):
            kocki = [j, j + 1, j + 2, j + 9, j + 10, j + 11, j + 18, j + 19, j + 20]
            problem.addConstraint(AllDifferentConstraint(), kocki)
    kolona = []
    for i in range(9):  # koloni
        kolona = range(i, i + 73, 9)  # vlagaat site koloni pochnuvajkji od prv index
        problem.addConstraint(AllDifferentConstraint(), kolona)

    redica = []
    for i in range(0, 73, 9):
        redica = range(i, i + 9) # vlagaat site redici pochnuvajkji od prv index
        problem.addConstraint(AllDifferentConstraint(), redica)

    problem.addVariables(variables, domain)

    print(problem.getSolution())

# from constraint import *
#
# if __name__ == '__main__':
#     solvers = {
#         'BacktrackingSolver': BacktrackingSolver(),
#         'RecursiveBacktrackingSolver': RecursiveBacktrackingSolver(),
#         'MinConflictsSolver': MinConflictsSolver()
#     }
#     problem = Problem(BacktrackingSolver())
#
#     variables = range(0, 81)
#     domain = range(1, 10)
#
#     problem.addVariables(variables, domain)
#
#     for i in range(0, 81, 9):
#         problem.addConstraint(AllDifferentConstraint(), range(i, i + 9))
#
#     for i in range(0, 9):
#         problem.addConstraint(AllDifferentConstraint(), range(i, 73 + i, 9))
#
#     for i in range(0, 61, 27):
#         for j in range(i, i + 9, 3):
#             problem.addConstraint(AllDifferentConstraint(), [j, j+1, j+2,
#                                                              j+9, j+10, j+11,
#                                                              j+18, j+19, j+20])
#
#     print(problem.getSolution())

