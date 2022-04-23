from constraint import *

if __name__ == '__main__':

# konsultacii: for ciklus kaj shto kje se biraat chlenovi, celata sum treba da e 100, ako ne e 100, mozhe i pomala

    num_members = int(input())
    members = {}  # lista ili rechnik

    for num in range(num_members):
        member = input()
        member = member.split(' ')

        mem_value = float(member[0])
        mem_name = str(member[1])

        members[mem_name] = mem_value

    # print(f'members: {members}')

    num_leaders = int(input())
    leaders = {}

    for num in range(num_leaders):
        leader = input()
        leader = leader.split(' ')

        lead_value = float(leader[0])
        lead_name = str(leader[1])

        leaders[lead_name] = lead_value

    # print(f'leaders: {leaders}')

    problem = Problem()

    problem.addVariables(range(1), list(leaders.keys()))
    problem.addVariables(range(1, 6), list(members.keys()))
    # problem.addConstraint(MaxSumConstraint(100))
    problem.addConstraint(AllDifferentConstraint())

    solutions = problem.getSolutions()

    max = 0
    names = []
    team = []

    print(solutions[0])
    for solution in solutions:
        names = solution.values()  # iminja - list

        values = []
        suma = 0
        for name in names:  # sekoe ime posebno
            # values.append([value for key, value in leaders.items() if key == name])

            suma += [value for key, value in leaders.items() if key == name]

        if suma > max and suma <= 100:
            max = suma
            team = solution

    print(team)

    print(f'Total score: {max}')
    leader_value = team[0]
    leader_name = [key for key, value in leaders.items() if value == leader_value]
    print(f'Team leader: {leader_name[0]}')

    for i in range(1, 6):
        member_value = team[i]
        member_name = [key for key, value in members.items() if value == member_value]
        print(f'Participant {i}: {member_name[0]}')
# 10
# 31.3 A
# 28.4 B
# 26.1 C
# 24.2 D
# 21.8 E
# 20.3 F
# 15.5 G
# 14.1 H
# 12.5 I
# 11.5 J
# 5
# 32.2 K
# 27.4 L
# 24.6 M
# 14.9 N
# 13.2 O
