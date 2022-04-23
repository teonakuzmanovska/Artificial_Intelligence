from constraint import *

if __name__ == "__main__":
    problem = Problem() #RecursiveBacktrackingSolver() #MinConflictsSolver()

    problem.addVariables(["WA", "NT", "SA", "Q", "NSW", "V", "T"], ["RED", "GREEN", "BLUE"])

    problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
    problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "NT"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
    problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
    problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
    problem.addConstraint(lambda a, b: a != b, ("NSW", "V"))

    solutions = problem.getSolution() #samo prvo reshenie
    #solutions = problem.getSolutions() #site reshenija
    print(solutions)