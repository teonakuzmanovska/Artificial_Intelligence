from searching_framework.utils import Problem
from searching_framework.informed_search import *

obstacles = [(0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2),
             (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6), (8, 5)]
#  7x9 frame
def move_right(atom1, atom2, atom3):
    while atom1[0] < 9 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        x = atom1[0]
        x += 1
        atom1 = x, atom1[1]
    pos_new = atom1[0] - 1, atom1[1]
    return pos_new


def move_left(atom1, atom2, atom3):
    while atom1[0] > -1 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        x = atom1[0]
        x += 1
        atom1 = x, atom1[1]
    pos_new = atom1[0] + 1, atom1[1]
    return pos_new


def move_up(atom1, atom2, atom3):
    while atom1[1] < 7 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        y = atom1[1]
        y += 1
        atom1 = atom1[0], y
    pos_new = atom1[0], atom1[1] - 1
    return pos_new


def move_down(atom1, atom2, atom3):
    while atom1[1] > -1 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        y = atom1[1]
        y -= 1
        atom1 = atom1[0], y
    pos_new = atom1[0], atom1[1] + 1
    return pos_new

class Molecule(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):

        successors = dict()

        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]

        # H1
        h1_new = move_right(h1, o, h2)
        state_new = h1_new, o, h2  # zasho sobiranje?
        if state_new != state:
            successors["RightH1"] = state_new

        h1_new = move_left(h1, o, h2)
        state_new = h1_new, o, h2  # zasho sobiranje?
        if state_new != state:
            successors["LeftH1"] = state_new

        h1_new = move_up(h1, o, h2)
        state_new = h1_new, o, h2  # zasho sobiranje?
        if state_new != state:
            successors["UpH1"] = state_new

        h1_new = move_down(h1, o, h2)
        state_new = h1_new, o, h2  # zasho sobiranje?
        if state_new != state:
            successors["DownH1"] = state_new

        # H2
        h2_new = move_right(h2, o, h1)
        state_new = h1, o, h2_new  # zasho sobiranje?
        if state_new != state:
            successors["RightH2"] = state_new

        h2_new = move_left(h2, o, h1)
        state_new = h1, o, h2_new  # zasho sobiranje?
        if state_new != state:
            successors["LeftH2"] = state_new

        h2_new = move_up(h2, o, h1)
        state_new = h1, o, h2_new  # zasho sobiranje?
        if state_new != state:
            successors["UpH2"] = state_new

        h2_new = move_down(h2, o, h1)
        state_new = h1, o, h2_new  # zasho sobiranje?
        if state_new != state:
            successors["DownH2"] = state_new

        # O
        o_new = move_right(o, h1, h2)
        state_new = h1, o_new, h2  # zasho sobiranje?
        if state_new != state:
            successors["RightH1"] = state_new

        o_new = move_left(o, h1, h2)
        state_new = h1, o_new, h2  # zasho sobiranje?
        if state_new != state:
            successors["LeftH1"] = state_new

        o_new = move_up(o, h1, h2)
        state_new = h1, o_new, h2  # zasho sobiranje?
        if state_new != state:
            successors["UpH1"] = state_new

        o_new = move_down(o, h1, h2)
        state_new = h1, o_new, h2  # zasho sobiranje?
        if state_new != state:
            successors["DownH1"] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]

        value = 0

        if h1[0] != o[0]:  # ne se vo ista redica
            if h1[1] != (o[1] - 1):  # ne e odma vo levata kolona
                value += 2
            else:  #odma vo levata kolona se naogja
                value += 1

        else:
            if h1[1] > o[1]:
                value += 3

            elif h1[0] < (o[1] - 1):
                value += 1

        if h2[0] != o[0]:
            if h2[1] != (o[1] + 1):
                value += 2
            else:
                value += 1
        else:  # h2[0] == o[0]
            if h2[1] < o[1]:
                value += 3
            elif h2[1] > (o[1] + 1):
                value += 1

        if h1[0] == h2[0] and h1[0] != o[0]:
            value -= 1  # posho sme presmetale turnuvanje i na h1 i na h2

        return value

    def goal_test(self, state):
        h1_x = state[0]
        h1_y = state[1]
        o_x = state[2]
        o_y = state[3]
        h2_x = state[4]
        h2_y = state[5]
        return h1_y == o_y == h2_y and h1_x == o_x - 1 and o_x == h2_x - 1


if __name__ == '__main__':

    h1_col = int(input())
    h1_row = int(input())
    o_col = int(input())
    o_row = int(input())
    h2_col = int(input())
    h2_row = int(input())

    molecule = Molecule((h1_col, h1_row, o_col, o_row, h2_col, h2_row))

    answer = astar_search(molecule)

    print(answer.solution())
