import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random
from math import fabs


class Cell:

    def __init__(self, terrain, representation, percentage, position=None):
        self.terrain = terrain
        self.percentage = percentage
        self.position = position
        self.representation = representation
        self.probability = 1/2500

    def get_cell_percentage(self):
        return self.percentage

    def get_cell_terrain(self):
        return self.terrain

    def get_cell_representation(self):
        return self.representation

    def __float__(self):
        return float(self.representation)

    def __repr__(self):
        return f'{self.position},{self.terrain}'

    def __str__(self):
        return f'{self.position},{self.terrain}'

    def __eq__(self, other):
        return self.position[0] == other.position[0] and self.position[1] == other.position[1]


def manhattan_distance(original_cell, cell):
    return fabs(cell.position[0] - original_cell.position[0]) + fabs(cell.position[1] - original_cell.position[1])


class Searchdestroy:
    def __init__(self, dim):
        self.fig, self.ax = plt.subplots(figsize=(7, 7))
        self.dim = dim
        """Cave = 1, Forest = 2, Flat = 3, Hilly = 4"""
        self.grid = np.random.choice(
            a=[Cell("cave", 0, .1), Cell("forest", 1, .3), Cell("hilly", 2, .7), Cell("flat", 3, .9)],
            size=(dim, dim),
            p=[.25, .25, .25, .25])
        self.target_location = (random.randint(0, self.dim - 1), random.randint(0, self.dim - 1))
        print("Snitch is located at", self.target_location)
        self.target_found = False
        self.probability_map = np.zeros(dim * dim)
        self.probability_map += (1 / (dim * dim))
        self.neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        print(self.grid)
        """        i = 0
        for x in range(self.dim):
            for y in range(self.dim):
                print(self.grid[x][y])
        # self.super_dumb_agent()
        self.second_basic_agent()
        """
        self.super_basic_agent_no_map()
        # self.display_grid()

    def display_grid(self):
        colormap = colors.ListedColormap(["blue", "green", "darkkhaki", "grey"])
        self.ax.imshow(self.grid, cmap=colormap, vmin=0, vmax=3)
        self.the_snitch(self.target_location[0], self.target_location[1])
        # print(self.grid[self.target_location[0]][self.target_location[1]].get_cell_type())
        plt.show()

    def the_snitch(self, x, y):
        self.ax.scatter(x, y, marker="*", color="cyan", s=50)

    def super_basic_agent(self):
        x, y = random.randint(0, self.dim - 1), random.randint(0, self.dim - 1)
        # x, y = 12, 15
        start_cell = old_cell = Cell(self.grid[x][y].get_cell_terrain(), self.grid[x][y].get_cell_representation(),
                                     self.grid[x][y].get_cell_percentage(), (x, y))
        cell_queue = []
        closed_cell_list = []
        cell_queue.append(start_cell)
        # closed_cell_list.append(start_cell)

        for q, u in self.neighbors:
            print(self.grid[x + q][y + u])
        j = 0
        while cell_queue:
            j += 1
            current_cell = cell_queue[0]
            current_index = 0

            # print(cell_queue)

            for index, cell in enumerate(cell_queue):
                if cell.percentage != current_cell.percentage:
                    if cell.percentage > current_cell.percentage:
                        current_cell = cell
                        current_index = index
                else:
                    if manhattan_distance(old_cell, cell) > manhattan_distance(old_cell, current_cell):
                        current_cell = cell
                        current_index = index
                    else:
                        if random.randint(1, 11) % 2 == 0:
                            current_cell = cell
                            current_index = index

            old_cell = cell_queue.pop(current_index)
            closed_cell_list.append(current_cell)

            x, y = current_cell.position[0], current_cell.position[1]

            """if the target is found, end the search loop"""
            print("Checking cell: ", current_cell)

            if random.uniform(0, 1) >= current_cell.get_cell_percentage() and \
                    current_cell.position[0] == self.target_location[0] and \
                    current_cell.position[1] == self.target_location[1]:
                self.target_found = True
                print("The target has been found at", current_cell.position)
                return True
            else:
                current_cell.probability *= 1 - current_cell.percentage
            for neighbor_x, neighbor_y in self.neighbors:
                if neighbor_x + x in range(self.dim) and neighbor_y + y in range(self.dim):
                    new_cell = Cell(self.grid[neighbor_x + x][neighbor_y + y].get_cell_terrain(),
                                    self.grid[neighbor_x + x][neighbor_y + y].get_cell_representation(),
                                    self.grid[neighbor_x + x][neighbor_y + y].get_cell_percentage(),
                                    (neighbor_x + x, neighbor_y + y))
                    if new_cell not in closed_cell_list:
                        cell_queue.append(new_cell)
                    # cell_list.append(new_cell)
            # print(cell_queue)
            # print(cell_list)

    def super_basic_agent_no_map(self):
        x, y = random.randint(0, self.dim - 1), random.randint(0, self.dim - 1)
        # x, y = 12, 15
        start_cell = old_cell = Cell(self.grid[x][y].get_cell_terrain(), self.grid[x][y].get_cell_representation(),
                                     self.grid[x][y].get_cell_percentage(), (x, y))
        cell_queue = []
        closed_cell_list = []
        cell_queue.append(start_cell)
        # closed_cell_list.append(start_cell)

        for q, u in self.neighbors:
            print(self.grid[x + q][y + u])
        j = 0
        while cell_queue:
            j += 1
            current_cell = cell_queue[0]
            current_index = 0

            # print(cell_queue)

            for index, cell in enumerate(cell_queue):
                if cell.percentage != current_cell.percentage:
                    if cell.percentage > current_cell.percentage:
                        current_cell = cell
                        current_index = index
                else:
                    if manhattan_distance(old_cell, cell) > manhattan_distance(old_cell, current_cell):
                        current_cell = cell
                        current_index = index
                    else:
                        if random.randint(1, 11) % 2 == 0:
                            current_cell = cell
                            current_index = index

            old_cell = cell_queue.pop(current_index)
            closed_cell_list.append(current_cell)

            x, y = current_cell.position[0], current_cell.position[1]

            """if the target is found, end the search loop"""
            print("Checking cell: ", current_cell)

            if random.uniform(0, 1) >= current_cell.get_cell_percentage() and \
                    current_cell.position[0] == self.target_location[0] and \
                    current_cell.position[1] == self.target_location[1]:
                print("Target has been found at: ", current_cell.position)
                self.target_found = True
                return True

            for neighbor_x, neighbor_y in self.neighbors:
                if neighbor_x + x in range(self.dim) and neighbor_y + y in range(self.dim):
                    new_cell = Cell(self.grid[neighbor_x + x][neighbor_y + y].get_cell_terrain(),
                                    self.grid[neighbor_x + x][neighbor_y + y].get_cell_representation(),
                                    self.grid[neighbor_x + x][neighbor_y + y].get_cell_percentage(),
                                    (neighbor_x + x, neighbor_y + y))
                    if new_cell not in closed_cell_list:
                        cell_queue.append(new_cell)
                    # cell_list.append(new_cell)
            # print(cell_queue)
            # print(cell_list)


if __name__ == '__main__':
    # dimension = int(input("Enter Dimension of the maze:\n"))
    search_and_destroy = Searchdestroy(50)
