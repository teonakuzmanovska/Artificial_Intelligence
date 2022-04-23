from searching_framework.utils import Problem
from searching_framework.informed_search import *


def update_obstacle_position(position):
    x, y, direction = position
    if(y == 0 and direction == -1) or (y == 5 and direction == 1):
        direction = direction * (-1)
    y_new = y + direction
    position_new = x, y_new, direction

    return position_new


def check_collision(man, obstacle1, obstacle2):
    return man != obstacle1[:2] and man != obstacle2[:2]


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):

        successors = dict()

        x = state[0]
        y = state[1]
        obstacle_1 = [state[2], state[3], state[4]]
        obstacle_2 = [state[5], state[6], state[7]]

        obstacle_1_new = update_obstacle_position(obstacle_1)
        obstacle_2_new = update_obstacle_position(obstacle_2)

        if x < 7:  # saka da se pridvizhi desno
            x_new = x + 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                successors["Right"] = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2], obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])  # initial

        if x > 0:  # saka da se pridvizhi levo
            x_new = x - 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                successors["Left"] = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2], obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

        if y < 5:  # saka da se pridvizhi gore
            x_new = x
            y_new = y + 1
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                successors["Up"] = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2], obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

        if y > 0:  # saka da se pridvizhi dole
            x_new = x
            y_new = y - 1
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                successors["Down"] = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2], obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

        return successors

    def h(self, node):
        x = node.state[0]
        y = node.state[1]

        h_x = self.goal[0]
        h_y = self.goal[1]

        return abs(x - h_x) + abs(y - h_y)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        g = self.goal
        return state[0] == g[0] and state[1] == g[1]  # x i y kooordinati


if __name__ == "__main__":

    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house = [house_x, house_y]

    explorer = Explorer((man_x, man_y, 2, 5, -1, 5, 0, 1), house)

    answer = astar_search(explorer)
    print(answer.solution())
