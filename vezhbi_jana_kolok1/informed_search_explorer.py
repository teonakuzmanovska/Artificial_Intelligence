from searching_framework.informed_search import *
from searching_framework.utils import *

class GraphExplorer(Problem):
    def __init__(self, initial, goal):
        super.__init__(initial, goal)

    def successor(self, state):
        player = state[0]
        links = state[2]

        successors = dict()

        # gore
        if player - 4 <= 1 and (player - 4, player) in links or (player, player - 4) in links:
            stars = tuple([x for x in state[1] if x != player - 4])
            new_links = [x for x in links if x != (player - 4, player) and (player, player - 4)]
            successors["gore"] = player - 4, stars, new_links

        # dole +4 TO DO
        if player + 4 <= 1 and (player + 4, player) in links or (player, player + 4) in links:
            stars = tuple([x for x in state[1] if x != player + 4])
            new_links = [x for x in links if x != (player + 4, player) and (player, player + 4)]
            successors["gore"] = player + 4, stars, new_links

        # levo -1 TO DO
        if player - 1 <= 1 and (player - 1, player) in links or (player, player - 1) in links:
            stars = tuple([x for x in state[1] if x != player - 1])
            new_links = [x for x in links if x != (player - 1, player) and (player, player - 1)]
            successors["gore"] = player - 1, stars, new_links

        # desno +1 TO DO
        if player + 1 <= 1 and (player + 1, player) in links or (player, player + 1) in links:
            stars = tuple([x for x in state[1] if x != player + 1])
            new_links = [x for x in links if x != (player + 1, player) and (player, player + 1)]
            successors["gore"] = player + 1, stars, new_links

        # gorelevo -1 TO DO
        if player % 4 != 1 and (player + 5, player) in links or (player, player + 5) in links:
            stars = tuple([x for x in state[1] if x != player + 5])
            new_links = [x for x in links if x != (player + 5, player) and (player, player + 5)]
            successors["gore"] = player + 5, stars, new_links

        # doledesno +1 TO DO
        if player % 4 != 1 and (player - 5, player) in links or (player, player - 5) in links:
            stars = tuple([x for x in state[1] if x != player - 5])
            new_links = [x for x in links if x != (player - 5, player) and (player, player - 5)]
            successors["gore"] = player - 5, stars, new_links


    def actions(self,state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(list(state[1])) == 0

    @staticmethod
    def euclidean(point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 1/2

    def h(self, node):
        min_score = 1000000000
        for star in node.state[1]:
            dist = self.euclidean(points[star], points[node.state[0]]) #treba da se definira rechnik
            if dist < min_score:
                min_score = dist

        return min_score

if __name__ == "__main__":
    player_position = int(input())
    star1 = int(input())
    star2 = int(input())

    initial_state = (player_position, (star1, star2))