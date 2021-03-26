import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random


class Cell:
    def __init__(self, type):
        self.type = type

        """indicated to be a 0 terrain type"""
        if self.type == "cave":
            self.percentage = .9
            self.representation = 0
            """indicated to be a 1 terrain type"""
        elif self.type == "forest":
            self.percentage = .7
            self.representation = 1
            """indicated to be a 2 terrain type"""
        elif self.type == "flat":
            self.percentage = .1
            self.representation = 2
            """indicated to be a 3 terrain type"""
        elif self.type == "hilly":
            self.percentage = .3
            self.representation = 3

    def get_cell_percentage(self):
        return self.percentage

    def get_cell_type(self):
        return self.type

    def __float__(self):
        return float(self.representation)

    def __repr__(self):
        return f'{self.representation}'

    def __str__(self):
        return f'{self.representation}'


class Search_Destroy:
    """Cust Maze"""

    def __init__(self, dim):
        self.fig, self.ax = plt.subplots(figsize=(7, 7))
        self.dim = dim
        self.grid = np.random.choice(
            a=[Cell("cave"), Cell("forest"), Cell("hilly"), Cell("flat")],
            size=(dim, dim),
            p=[.25, .25, .25, .25])
        self.target_location = (random.randint(0, self.dim - 1), random.randint(0, self.dim - 1))
        self.target_found = False
        self.display_grid()

    def display_grid(self):
        colormap = colors.ListedColormap(["grey", "green", "darkkhaki", "darkgreen"])
        self.ax.imshow(self.grid.astype(np.float), cmap=colormap)
        self.the_snitch(self.target_location[0], self.target_location[1])
        print(self.grid[self.target_location[0]][self.target_location[1]].get_cell_type())
        plt.show()

    def the_snitch(self, x, y):
        self.ax.scatter(x, y, marker="*", color="cyan", s=50)

    def super_dumb_agent(self):
        pass


if __name__ == '__main__':
    dimension = int(input("Enter Dimension of the maze:\n"))
    search_and_destroy = Search_Destroy(dimension)
