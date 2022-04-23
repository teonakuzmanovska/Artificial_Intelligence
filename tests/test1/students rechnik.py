class Subject:
    def __init__(self, sub, thr, prc, lab):
        self.subject_subject = sub
        self.subject_theory = thr
        self.subject_practical = prc
        self.subject_labs = lab

    def grade(self):

        points = float(self.subject_theory) + float(self.subject_practical) + float(self.subject_labs)

        if 0 <= points <= 50:
            return 5
        elif 50 < points <= 60:
            return 6
        elif 60 < points <= 70:
            return 7
        elif 70 < points <= 80:
            return 8
        elif 80 < points <= 90:
            return 9
        elif 90 < points <= 100:
            return 10


class Student:
    def __init__(self, nm, snm):
        self.student_name = nm
        self.student_surname = snm
        self.student_subjects = []  # initially empty, probaj da ja ispechatish

    def add_subject(self, subs):  # se izvrshuva i koga se kreira i koga ne se kreira nov student
        self.student_subjects.append(subs)

    # ----Artificial Intelligence: 9
    # ----Machine Learning: 8      return msg

    def print_subject(self):
        strng = ""
        for sbj in self.student_subjects:
            strng += "----" + sbj.subject_subject + ": " + str(sbj.grade()) + "\n"
        return strng


if __name__ == "__main__":

    students = {}
    while True:
        vlez = input()

        if vlez == "end":
            break

        elements = vlez.split(",")
        input_name = elements[0]
        input_surname = elements[1]
        input_index = elements[2]
        input_subject = elements[3]
        input_theory = elements[4]
        input_practical = elements[5]
        input_labs = elements[6]

        if input_index not in students:
            students[input_index] = Student(input_name, input_surname)  # kreiraj nov student

        new_subject = Subject(input_subject, input_theory, input_practical, input_labs)  # dodadi nov predmet na studentot (zaedno so poenite za istiot)
        students[input_index].add_subject(new_subject)

    for std in students:
        print(f"Student: {students[std].student_name} {students[std].student_surname}\n{students[std].print_subject()}")
