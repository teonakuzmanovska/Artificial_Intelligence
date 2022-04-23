from constraint import *


# def my_constraint(marija, petar, simona):
#     if marija != petar and simona == marija:
#         return True
# #         marija ide na sostanok
#     if marija != petar and simona == petar:
#         return True
# #         petar ide na sostanok
#     else:
#         return False
# #         nema sostanok


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [13, 14, 16, 19])  # togash mozhe simona
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------

    # Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
    # Марија слободни термини: 14:00-16:00, 18:00-19:00
    # Петар слободни термини: 12:00-14:00, 16:00-20:00

    # marija_vreme = [14, 15, 18]
    # simona_vreme = [13, 14, 16, 19]
    # petar_vreme = [12, 13, 16, 17, 18, 19]
    # vreme_sostanok = [13, 14, 16, 19]

    # m, s, p = 0
    # while m < len(marija_vreme):
    #     while s < len(simona_vreme):
    #         while p < len(petar_vreme):
    #             problem.addConstraint(my_constraint, (marija_vreme[m], petar_vreme[p], simona_vreme[s]))
    #             p += 1
    #         s += 1
    #     m += 1

    # Constraints:
    # petar i marija mora da se razlichni (0 i 1)
    # simona i marija smeat samo vo 14
    # simona i petar smeat vo 13, 16, 19
    # simona ne smee da e sama

    # problem.addConstraint(lambda a, b: a == 0 or a == 1 and b == 13 or a == 1 and b == 16 or a == 1 and b == 19, ("Petar_prisustvo", "vreme_sostanok"))
    # problem.addConstraint(lambda a, b: a == 1 and b == 13 or a == 1 and b == 16 or a == 1 and b == 19, ("Petar_prisustvo", "vreme_sostanok"))
    problem.addConstraint(lambda a, b: a == 0 or b == 14 or b == 15 or b == 20, ("Petar_prisustvo", "vreme_sostanok"))

    problem.addConstraint(lambda a, b, c: a + b + c > c, ("Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))

    # problem.addConstraint(lambda a, b: a == 0 or a == 1 and b == 14, ("Marija_prisustvo", "vreme_sostanok"))
    # problem.addConstraint(lambda a, b: a == 1 and b == 14, ("Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(lambda a, b: a == 0 or a + b == 15, ("Marija_prisustvo", "vreme_sostanok"))

    [print(solution) for solution in problem.getSolutions()]

# {'vreme_sostanok': 19, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'Simona_prisustvo': 1}
# {'vreme_sostanok': 16, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'Simona_prisustvo': 1}
# {'vreme_sostanok': 14, 'Petar_prisustvo': 0, 'Marija_prisustvo': 1, 'Simona_prisustvo': 1}
# {'vreme_sostanok': 13, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'Simona_prisustvo': 1}

# {'vreme_sostanok': 14, 'Marija_prisustvo': 1, 'Petar_prisustvo': 1, 'Simona_prisustvo': 1}
# {'vreme_sostanok': 14, 'Marija_prisustvo': 1, 'Petar_prisustvo': 0, 'Simona_prisustvo': 1}
# {'vreme_sostanok': 14, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'Simona_prisustvo': 1}
