from Ant import *
from data import edges_df, edges
import numpy as np
import pandas as pd


class Aco:
    def __init__(self, rho, Q, k):
        self.rho = rho
        self.k = k
        self.Q = Q

    def get_trajectories(self, initial_node, end_node):
        trajectories = []
        distances = []
        while self.k > 0:
            ant = Ant(edges_df, 1, 1)
            trajectory = ant.get_trajectory(initial_node, end_node)
            trajectories.append(tuple(trajectory))
            distances.append(ant.distance_traveled(trajectory))
            self.k = self.k-1
        ants_df = pd.DataFrame(distances, index=trajectories)
        return ants_df

    def update_pheromone(self, ants_df):

        for edge in edges:
            delta = 0
            for i in range(len(ants_df)):
                if edge in ants_df.index.values.tolist()[i]:
                    delta = delta + self.Q / (ants_df.values[i][0])
            edge.set_pheromone((1 - self.rho) * edge.get_pheromone() + delta)

    def get_best_route(self, updated_routes):
        the_best_route = updated_routes[updated_routes[0] == min(updated_routes[0].values)].index.values
        return the_best_route

