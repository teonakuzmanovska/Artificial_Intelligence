# from constraint import *
#
# if __name__ == "__main__":
#     problem = Problem() #RecursiveBacktrackingSolver() #MinConflictsSolver()
#
#     problem.addVariables(["A", "B", "C", "D"], ["lion", "tiger", "parrot", "deer", "giraffe", "python", "gazelle"])
#
#     #problem.addConstraint(lambda a, b: a == b, ("lion", "A"))  # ?
#
#
#     problem.addConstraint(lambda a, b, c, d, e: a != b and a != c and a != d and a != e, ("lion", "tiger", "python", "deer", "parrot"))
#     problem.addConstraint(lambda a, b: a == b, ("giraffe", "gazelle"))
#     problem.addConstraint(lambda a, b, c, d, e: a != b and a != c and a != d and a != e, ("python", "lion", "giraffe", "deer", "parrot", "gazelle"))
#
#     solutions = problem.getSolution() #samo prvo reshenie
#     #solutions = problem.getSolutions() #site reshenija
#     print(solutions)



