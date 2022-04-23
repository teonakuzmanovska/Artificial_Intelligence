from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
# zasho nekogash stavame if x - 1 > 0, a nekogash x > 0 i vo koi sluchaevi koe se stava?
def k1(k_x, k_y, b_x, b_y):
    if k_x - 1 > 0 and k_y + 2 < 8 and [k_x - 1, k_y + 2] != [b_x, b_y]:
        k_x -= 1
        k_y += 2
    return k_x, k_y

def k2(k_x, k_y, b_x, b_y):
    if k_x + 1 < 8 and k_y + 2 < 8 and [k_x + 1, k_y + 2] != [b_x, b_y]:
        k_x += 1
        k_y += 2
    return k_x, k_y

def k3(k_x, k_y, b_x, b_y):
    if k_x + 2 < 8 and k_y + 1 < 8 and [k_x + 2, k_y + 1] != [b_x, b_y]:
        k_x += 2
        k_y += 1
    return k_x, k_y

def k4(k_x, k_y, b_x, b_y):
    if k_x + 2 < 8 and k_y - 1 > 0 and [k_x + 2, k_y - 1] != [b_x, b_y]:
        k_x += 2
        k_y -= 1
    return k_x, k_y

def k5(k_x, k_y, b_x, b_y):
    if k_x + 1 < 8 and k_y - 2 > 0 and [k_x + 1, k_y - 2] != [b_x, b_y]:
        k_x += 1
        k_y -= 2
    return k_x, k_y

def k6(k_x, k_y, b_x, b_y):
    if k_x - 1 > 0 and k_y - 2 > 0 and [k_x - 1, k_y - 2] != [b_x, b_y]:
        k_x -= 1
        k_y -= 2
    return k_x, k_y

def k7(k_x, k_y, b_x, b_y):
    if k_x - 2 > 0 and k_y - 1 > 0 and [k_x - 2, k_y - 1] != [b_x, b_y]:
        k_x -= 2
        k_y -= 1
    return k_x, k_y

def k8(k_x, k_y, b_x, b_y):
    if k_x - 2 > 0 and k_y + 1 < 8 and [k_x - 2, k_y + 1] != [b_x, b_y]:
        k_x -= 2
        k_y += 1
    return k_x, k_y

def b1(b_x, b_y, k_x, k_y):  #gore-levo
    if b_x - 1 > 0 and b_y + 1 < 8 and [b_x - 1, b_y + 1] != [k_x, k_y]:
        b_x -= 1
        b_y += 1
    return b_x, b_y

def b2(b_x, b_y, k_x, k_y):  #gore-desno
    if b_x + 1 < 8 and b_y + 1 < 8 and [b_x + 1, b_y + 1] != [k_x, k_y]:
        b_x += 1
        b_y += 1
    return b_x, b_y

def b3(b_x, b_y, k_x, k_y):  # dole-levo
    if b_x - 1 > 0 and b_y - 1 > 0 and [b_x - 1, b_y - 1] != [k_x, k_y]:
        b_x -= 1
        b_y -= 1
    return b_x, b_y

def b4(b_x, b_y, k_x, k_y):  # dole-desno
    if b_x + 1 < 8 and b_y - 1 > 0 and [b_x + 1, b_y - 1] != [k_x, k_y]:
        b_x += 1
        b_y -= 1
    return b_x, b_y

class Stars(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        knight_x = state[0]
        knight_y = state[1]
        bishop_x = state[2]
        bishop_y = state[3]

        stars_positions = state[4]
        #proveri dali se mrdaat, sobiraj dzvezdi

        new_kx, new_ky = k1(knight_x, knight_y, bishop_x, bishop_y) #vrakja 2 argumenti
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K1"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky])) # dzvezdite se tuple od tuples
        new_kx, new_ky = k2(knight_x, knight_y, bishop_x, bishop_y)  # vrakja 2 argumenti

        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K2"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_kx, new_ky = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K3"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_kx, new_ky = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K4"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_kx, new_ky = k5(knight_x, knight_y, bishop_x, bishop_y)
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K5"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_kx, new_ky = k6(knight_x, knight_y, bishop_x, bishop_y)
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K6"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_kx, new_ky = k7(knight_x, knight_y, bishop_x, bishop_y)
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K7"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_kx, new_ky = k8(knight_x, knight_y, bishop_x, bishop_y)
        if [new_kx, new_ky] != [knight_x, knight_y]:
            successors["K8"] = (new_kx, new_ky, bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_kx or s[1] != new_ky]))

        new_bx, new_by = b1(bishop_x, bishop_y, knight_x, knight_y)
        if [new_bx, new_by] != [bishop_x, bishop_y]:
            successors["B1"] = (new_bx, new_by, knight_x, knight_y,
                                tuple([s for s in stars_positions if s[0] != new_bx or s[1] != new_by]))

        new_bx, new_by = b2(bishop_x, bishop_y, knight_x, knight_y)
        if [new_bx, new_by] != [bishop_x, bishop_y]:
            successors["B2"] = (new_bx, new_by, knight_x, knight_y,
                                tuple([s for s in stars_positions if s[0] != new_bx or s[1] != new_by]))

        new_bx, new_by = b3(bishop_x, bishop_y, knight_x, knight_y)
        if [new_bx, new_by] != [bishop_x, bishop_y]:
            successors["B3"] = (new_bx, new_by, knight_x, knight_y,
                                tuple([s for s in stars_positions if s[0] != new_bx or s[1] != new_by]))

        new_bx, new_by = b4(bishop_x, bishop_y, knight_x, knight_y)
        if [new_bx, new_by] != [bishop_x, bishop_y]:
            successors["B4"] = (new_bx, new_by, knight_x, knight_y,
                                tuple([s for s in stars_positions if s[0] != new_bx or s[1] != new_by]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0

if __name__ == '__main__':

    stars_pos = ((1, 1), (4, 3), (6, 6))
    knight = [2, 5]
    bishop = [5, 1]

    stars = Stars((knight[0], knight[1], bishop[0], bishop[1], stars_pos))

    result = breadth_first_graph_search(stars)
    print(result.solution())