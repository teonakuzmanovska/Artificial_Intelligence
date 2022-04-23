from constraint import *

# 0  1  2  | 3  4  5  | 6  7  8  (0 * 9 + 2 za 2) -> konvertiranje, na kraj otkako kje se dobijat constraints
# 9  10 11 | 12 13 14 | 15 16 17 (+-1 od centralen element) -> uslov za kvadrat
# 18 19 20 | 21 22 23 | 24 25 26
# ------------------------------
# 27 28 29 | 30 31 32 | 33 34 35
# 36 37 38 | 39 40 41 | 42 43 44
# 45 46 47 | 48 49 50 | 51 52 53  (5 * 9 + 2 za 47) -> i * 9 + j
# ------------------------------
# 54 55 56 | 57 58 59 | 60 61 62
# 63 64 65 | 66 67 68 | 69 70 71
# 72 73 74 | 75 76 77 | 78 79 80


# [0, 0], [0, 1], [0, 2] | [0, 3], [0, 4], [0, 5] | [0, 6], [0, 7], [0, 8]
# [1, 0], [1, 1], [1, 2] | [1, 3], [1, 4], [1, 5] | [1, 6], [1, 7], [1, 8]
# [2, 0], [2, 1], [2, 2] | [2, 3], [2, 4], [2, 5] | [2, 6], [2, 7], [2, 8]
# ------------------------------------------------------------------------
# [3, 0], [3, 1], [3, 2] | [3, 3], [3, 4], [3, 5] | [3, 6], [3, 7], [3, 8]
# [4, 0], [4, 1], [4, 2] | [4, 3], [4, 4], [4, 5] | [4, 6], [4, 7], [4, 8]
# [5, 0], [5, 1], [5, 2] | [5, 3], [5, 4], [5, 5] | [5, 6], [5, 7], [5, 8]
# ------------------------------------------------------------------------
# [6, 0], [6, 1], [6, 2] | [6, 3], [6, 4], [6, 5] | [6, 6], [6, 7], [6, 8]
# [7, 0], [7, 1], [7, 2] | [7, 3], [7, 4], [7, 5] | [7, 6], [7, 7], [7, 8]
# [8, 0], [8, 1], [8, 2] | [8, 3], [8, 4], [8, 5] | [8, 6], [8, 7], [8, 8]

# def my_constraint(f1, f2):
#     i_1 = f1[0]
#     j_1 = f1[1]
#     i_2 = f2[0]
#     j_2 = f2[1]
#     if i_1 == i_2 or j_1 == j_2 or abs(i_1 - i_2) == abs(j_1 - j_2):
#         return False
#     else:
#         return True

if __name__ == '__main__':

    solver = input()
    if solver == "BackTrackingSolver":
        problem = Problem(BacktrackingSolver())
    if solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    if solver == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())

    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    coordinates = []
    variables = range(81)

    for i in range(9):
        for j in range(9):
            coordinates.append((i, j))
            #domain.append(i * 9 + j)

    # for variable in variables:
    #     problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addVariables(variables, domain)  # coordinates ili domain?

    for field1 in coordinates:
        for field2 in coordinates:
            i1 = field1[0]
            j1 = field1[1]
            i2 = field2[0]
            j2 = field2[1]
            if (field1 != field2) and (i1 == i2 or j1 == j2):  # ist red
                problem.addConstraint(AllDifferentConstraint(), variables)
            if (field1 != field2) and (i1 == 1 or i1 == 4 or i1 == 7) and (j1 == 1 or j1 == 4 or j1 == 7) and (abs(i1 - i2) == abs(j1 - j2)):  #ista kocka, centralen element
                # vaka se proveruva samo za srednite elementi
                problem.addConstraint(AllDifferentConstraint(), variables)

    # ----------------------------------------------------

    print(problem.getSolution())


