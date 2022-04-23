class Subject:
    def __init__(self, n, t, p, lab):
        self.s_name = n
        self.s_theory = t
        self.s_practice = p
        self.s_labs = lab

    def calculate_grade(self):
        points = float(self.s_theory) + float(self.s_practice) + float(self.s_labs)
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
        else:
            return 10


class Student:
    def __init__(self, n, sn):
        self.name = n
        self.surname = sn
        self.subjects = []

    def add_subject(self, s):
        self.subjects.append(s)

    def print_subjects(self):
        msg = ""
        for element in self.subjects:
            msg += "----" + element.s_name + ": " + str(element.calculate_grade()) + "\n"
        return msg


if __name__ == "__main__":
    students = {}
    while True:
        studentInput = input()
        if studentInput == "end":
            break
        inputSegs = studentInput.split(',')
        name = inputSegs[0]
        surname = inputSegs[1]
        index = inputSegs[2]
        subject = inputSegs[3]
        theory = inputSegs[4]
        practice = inputSegs[5]
        labs = inputSegs[6]

        if index not in students:
            students[index] = Student(name, surname)
        students[index].add_subject(Subject(subject, theory, practice, labs))

    for key in students:
        print(f"Student: {students[key].name} {students[key].surname}\n{students[key].print_subjects()}")