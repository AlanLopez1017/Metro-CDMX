import pandas as pd
import numpy as np
from data import nodes, edges_df


class Ant:

    def __init__(self, available_routes, alpha, beta):
        self.available_routes = available_routes
        self.alpha = alpha
        self.beta = beta
        self.trajectory = []

    def possible_routes(self, initial_node):
        poss_routes = [edges_df._get_value(pe, "edges") for pe in self.available_routes.index if
                       nodes.index(initial_node) + 1 in pe]
        return poss_routes

    def get_chosen_route(self, poss_routes):
        prob_routes = []
        den = 0
        random = np.random.rand(1)
        for pr in poss_routes:
            value = (pr.get_pheromone()**self.alpha) * (pr.get_visibility()**self.beta)
            prob_routes.append(value)
            den = den + value
        prob_routes = np.array(prob_routes)/den
        prob_routes_cumulative = np.cumsum(prob_routes)
        lista = list(np.where(random > prob_routes_cumulative, prob_routes, 0))
        chosen_route = lista.index(next(filter(lambda x: x == 0, lista)))
        return chosen_route

    def get_trajectory(self, initial_node, end_node):
        cond = False
        while initial_node != end_node:
            chosen_route = self.get_chosen_route(self.possible_routes(initial_node))
            edgeee = self.possible_routes(initial_node)[chosen_route]

            if cond:
                self.available_routes = pd.concat(
                    [self.available_routes, pd.DataFrame(self.value, index=[self.key], columns=["edges"])])

            if initial_node == edgeee.get_node2():
                initial_node = self.possible_routes(initial_node)[chosen_route].get_node1()
            else:
                initial_node = self.possible_routes(initial_node)[chosen_route].get_node2()
            self.key = self.available_routes.index[self.available_routes["edges"] == edgeee][0]
            self.value = edgeee
            self.available_routes = self.available_routes.drop(
                self.available_routes.index[self.available_routes["edges"] == edgeee])

            self.trajectory.append(edgeee)
            cond = True
        return self.trajectory

    def distance_traveled(self, routes):
        distance = [route.get_distance() for route in routes]
        return np.array(distance).sum()
