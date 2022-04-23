from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)  # to do : smeni super ako ima error
        self.grid_size = [8, 6]  # nie si go dodadovme

    def successor(self, state):
        successors = dict()

        # man_x = int(state[0])
        # man_y = int(state[1])
        # obstacle_1 = list(state[2])  # treba da se dvizhi down (2, 5, 1)
        # obstacle_2 = list(state[3])  # treba da se dvizhi up (5,0)

        man_x = state[0]
        man_y = state[1]
        obstacle_1 = [state[2], state[3], state[4]]
        obstacle_2 = [state[5], state[6], state[7]]

        max_x = self.grid_size[0]  # neli mozheshe samo max_x = 8, mesto da sozdavame torka grid_size
        max_y = self.grid_size[1]

        # proveruvame za prvata prechka
        if obstacle_1[2] == 0:  # treba da ide up
            if obstacle_1[1] == max_y:  # ako stignala do gore
                obstacle_1[2] = 1  # smeni pravec (treba da idesh down)
                obstacle_1[1] -= 1
            else:
                obstacle_1[1] += 1

        else:  # treba da ide down
            if obstacle_1[1] == 0:  # ako stignala do dole
                obstacle_1[2] = 0  # smeni pravec (treba da idesh up)
                obstacle_1[1] += 1
            else:
                obstacle_1[1] -= 1

        # proveruvame za vtorata prechka
        if obstacle_2[2] == 0:  # treba da ide up
            if obstacle_2[1] == max_y:  # ako stignala do gore
                obstacle_2[2] = 1  # smeni pravec (treba da idesh down)
                obstacle_2[1] -= 1
            else:
                obstacle_2[1] += 1

        else:  # treba da ide down
            if obstacle_2[1] == 0:  # ako stignala do dole
                obstacle_2[2] = 0  # smeni pravec (treba da idesh up)
                obstacle_2[1] += 1
            else:
                obstacle_2[1] -= 1

        obstacles = [[obstacle_1[0], obstacle_1[1]], [obstacle_2[0], obstacle_2[1]]]  # updated obstacles
        # man

        if man_x < max_x - 1 and [man_x + 1, man_y] not in obstacles:  # saka da se pridvizhi desno
            successors["Right"] = (man_x + 1, man_y, obstacle_1[0], obstacle_1[1], obstacle_1[2], obstacle_2[0], obstacle_2[1], obstacle_2[2])  # initial

        if man_x > 0 and [man_x - 1, man_y] not in obstacles:  # saka da se pridvizhi levo
            successors["Left"] = (man_x - 1, man_y, obstacle_1[0], obstacle_1[1], obstacle_1[2], obstacle_2[0], obstacle_2[1], obstacle_2[2])

        if man_y < max_y - 1 and [man_x, man_y + 1] not in obstacles:  # saka da se pridvizhi gore
            successors["Up"] = (man_x, man_y + 1, obstacle_1[0], obstacle_1[1], obstacle_1[2], obstacle_2[0], obstacle_2[1], obstacle_2[2])

        if man_y > 0 and [man_x, man_y - 1] not in obstacles:  # saka da se pridvizhi dole
            successors["Down"] = (man_x, man_y - 1, obstacle_1[0], obstacle_1[1], obstacle_1[2], obstacle_2[0], obstacle_2[1], obstacle_2[2])

        # if man_x < max_x - 1 and [man_x + 1, man_y] not in (obstacle_1, obstacle_2):  # saka da se pridvizhi desno
        #     successors["Right"] = (man_x + 1, man_y, tuple(obstacle_1), tuple(obstacle_2))  # initial
        #
        # if man_x > 0 and [man_x - 1, man_y] not in (obstacle_1, obstacle_2):  # saka da se pridvizhi levo
        #     successors["Left"] = (man_x - 1, man_y, tuple(obstacle_1), tuple(obstacle_2))
        #
        # if man_y < max_y - 1 and [man_x, man_y + 1] not in (obstacle_1, obstacle_2):  # saka da se pridvizhi gore
        #     successors["Up"] = (man_x, man_y + 1, tuple(obstacle_1), tuple(obstacle_2))
        #
        # if man_y > 0 and [man_x, man_y - 1] not in (obstacle_1, obstacle_2):  # saka da se pridvizhi dole
        #     successors["Down"] = (man_x, man_y - 1, tuple(obstacle_1), tuple(obstacle_2))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0], state[1])
        return position == self.goal


if __name__ == "__main__":
    goal_state = (7, 4)
    initial_state = (0, 2)
    obstacle1 = (2, 5, 1)  # treba da se dvizhi down (2,5) koordinati, 1 pravec
    obstacle2 = (5, 0, 0)  # treba da se dvizhi up (5,0) koordinati, 0 pravec

    explorer = Explorer(
        (initial_state[0], initial_state[1], obstacle1[0], obstacle1[1], obstacle1[2], obstacle2[0], obstacle2[1], obstacle2[2]),
        goal_state
    )

    # explorer = Explorer(
    #     (initial_state[0], initial_state[1], obstacle1, obstacle2),
    #     goal_state
    # )

    print(breadth_first_graph_search(explorer).solution())
    print(breadth_first_graph_search(explorer).solve())

