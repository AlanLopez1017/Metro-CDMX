#from Node import *
import numpy as np


class Node:

    def __init__(self, position: np.ndarray, name: str):
        self._name = name
        self._position = position

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def __str__(self):
        return "Node {} located in ({})".format(self._name, self._position)


class Edge:

    def __init__(self, node1, node2, pheromone, name, color):
        self._node1 = node1
        self._node2 = node2
        self._pheromone = pheromone
        self._color = color
        self._name = name

    def set_pheromone(self, pheromone: float) -> None:
        self._pheromone = pheromone

    def get_node1(self):
        return self._node1

    def get_node2(self):
        return self._node2

    def get_pheromone(self):
        return self._pheromone

    def get_visibility(self):
        return self._visibility

    def get_distance(self):
        distance = np.sqrt((self._node1.get_position()[0] - self._node2.get_position()[0]) ** 2 +
                                 (self._node1.get_position()[1] - self._node2.get_position()[1]) ** 2)/200
        return distance

    def get_visibility(self):
        visibility = 1/self.get_distance()
        return visibility

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def __str__(self):
        return "Route {}".format(self._name)

