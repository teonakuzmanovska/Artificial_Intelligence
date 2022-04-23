from searching_framework.uninformed_search import *
from searching_framework.utils import Problem


class Container(Problem):

    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)

        self.capacities = capacities  #kolku sobira max u sadot

    def successor(self, state):
        successors = dict()

        x, y = state  #j0 i j1
        c0, c1 = self.capacities  #j0 i j1

        if x > 0:
            successors["Isprazni go sadot J0"] = (0, y)

        if y > 0:
            successors["Isprazni go sadot J1"] = (x, 0)

        if x > 0 and y < c1:
            delta = min(x, c1 - y)
            successors["Preturi od j0 vo j1"] = (x - delta, y + delta)

        if y > 0 and x < c0:
            delta = min(y, c0 - x)
            successors["Preturi od j1 vo j0"] = (x + delta, y - delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == "__main__":

    container = Container([15, 5], (5, 5), (10, 0))

    result = breadth_first_graph_search(container)

    print(result.solution())
