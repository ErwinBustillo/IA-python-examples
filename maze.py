from __future__ import print_function

import math
from simpleai.search import SearchProblem, astar

MAP = """
##############################
#o         #              #  #
# ####    ########       #   #
#    #    #              #   #
#    ###  #  ####   ######   #
#      #  ####      #        #
#      #     #  #   #   #### #
#     #####     #       # x  #
#               #            #
##############################
"""
MAP = [list(x) for x in MAP.split("\n") if x]

COSTS = {
    "ARRIBA": 1.0,
    "ABAJO": 1.0,
    "IZQUIERDA": 1.0,
    "DERECHA": 1.0,
}


class MazeProblem(SearchProblem):

    def __init__(self, board):
        self.board = board
        self.goal = (0, 0)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.goal = (x, y)

        super(MazeProblem, self).__init__(initial_state=self.initial)

    def actions(self, state):
        actions = []
        for action in list(COSTS.keys()):
            newx, newy = self.result(state, action)
            if self.board[newy][newx] != "#":
                actions.append(action)
        return actions

    def result(self, state, action):
        x, y = state

        if action.count("ARRIBA"):
            y -= 1
        if action.count("ABAJO"):
            y += 1
        if action.count("IZQUIERDA"):
            x -= 1
        if action.count("DERECHA"):
            x += 1

        new_state = (x, y)
        return new_state

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return COSTS[action]

    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


def main():
    problem = MazeProblem(MAP)
    result = astar(problem, graph_search=True)
    path = [x[1] for x in result.path()]
    # RECORRE EL RESULTADO PARA PINTARLO EN EL MAPA
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if (x, y) == problem.initial:
                print("o", end='')
            elif (x, y) == problem.goal:
                print("x", end='')
            elif (x, y) in path:
                print("·", end='')
            else:
                print(MAP[y][x], end='')
        print()


if __name__ == "__main__":
    main()
