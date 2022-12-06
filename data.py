import numpy as np
from Edge import *
import pandas as pd
nodes_name = ["El Rosario", "Instituto \ndel Petroleo", "Deportivo 18 \nde Marzo",
         "Martin Carrera", "La Raza", "Tacuba", "Guerrero", "Garibaldi",
         "Hidalgo", "Bellas Artes", "Consulado", "Morelos", "San Lazaro",
         "Candelaria", "Oceania", "Balderas", "Salto del Agua", "Pino Suarez",
         "Tacubaya", "Centro Medico", "Chabacano", "Jamaica", "Pantitlan", "Santa Anita"]

pos = np.int64((np.array([[169,23],[416,68],[529,68],[736,68],[482,134],[169,214],[416,251],
                [501,251],[416,290],[501,290],[736,185],[736,285],[779,324],[736,324],
                [893,275],[416,425],[501,425],[613,425],[169,572],[416,572],[613,572],[736, 572],[960,528],[736,645]])*1.4)+np.array([-170,60]))

paths = [(1,2), (2,3), (3,4), (2,5), (3,5), (5,11), (4,11), (1,6), (5,7),(6,19),(6,9),(19,16),(7,9),(9,16),(16,20),
         (19,20),(7,8),(8,10),(9,10),(10,17),(16,17),(20,21),(17,21),(10,18),(18,21),(17,18),(8,12),(12,14),(12,13),(13,14),
         (14,18),(14,22),(21,22),(11,12),(11,15),(13,15),(13,23),(22,23),(15,23),(21,24),(22,24)]

nodes = []
edges = []
for i, v in enumerate(nodes_name):
    nodes.append(Node(pos[i], v))

pheromone = 0.1

edges = [Edge(nodes[0],nodes[1],pheromone,paths[0], '#d9251d'), Edge(nodes[1],nodes[2],pheromone, paths[1],'#d9251d'), Edge(nodes[2],nodes[3],pheromone, paths[2],'#d9251d'),
         Edge(nodes[1],nodes[4],pheromone, paths[3], '#f9c114'), Edge(nodes[2],nodes[4],pheromone, paths[4],'#9e993e'), Edge(nodes[4],nodes[10],pheromone, paths[5],'#f9c114'),
         Edge(nodes[3],nodes[10],pheromone, paths[6],'#95d1ba'),Edge(nodes[0],nodes[5],pheromone, paths[7],'#ec9639'),Edge(nodes[4],nodes[6],pheromone, paths[8],'#9e993e'),
         Edge(nodes[5],nodes[18],pheromone, paths[9],'#ec9639'),Edge(nodes[5],nodes[8],pheromone, paths[10],'#007ec3'),Edge(nodes[18],nodes[15],pheromone, paths[11],'#d55893'),
         Edge(nodes[6],nodes[8],pheromone, paths[12],'#9e993e'),Edge(nodes[8],nodes[15],pheromone, paths[13],'#9e993e'),Edge(nodes[15],nodes[19],pheromone, paths[14],'#9e993e'),
         Edge(nodes[18],nodes[19],pheromone, paths[15],'#8b543f'),Edge(nodes[6],nodes[7],pheromone, paths[16],'#a8a8a8'),Edge(nodes[7],nodes[9],pheromone, paths[17],'#03913e'),
         Edge(nodes[8],nodes[9],pheromone, paths[18],'#007ec3'),Edge(nodes[9],nodes[16],pheromone, paths[19],'#03913e'),Edge(nodes[15],nodes[16],pheromone, paths[20],'#d55893'),
         Edge(nodes[19],nodes[20],pheromone, paths[21],'#8b543f'),Edge(nodes[16],nodes[20],pheromone, paths[22],'#03913e'),Edge(nodes[9],nodes[17],pheromone, paths[23],'#007ec3'),
         Edge(nodes[17],nodes[20],pheromone, paths[24],'#007ec3'),Edge(nodes[16],nodes[17],pheromone, paths[25],'#d55893'), Edge(nodes[7],nodes[11],pheromone, paths[26],'#a8a8a8'),
         Edge(nodes[11],nodes[13],pheromone, paths[27],'#95d1ba'),Edge(nodes[11],nodes[12],pheromone, paths[28],'#a8a8a8'),Edge(nodes[12],nodes[13],pheromone, paths[29],'#d55893'),
         Edge(nodes[13],nodes[17],pheromone, paths[30],'#d55893'),Edge(nodes[13],nodes[21],pheromone, paths[31],'#95d1ba'),Edge(nodes[20],nodes[21],pheromone, paths[32],'#8b543f'),
         Edge(nodes[10],nodes[11],pheromone, paths[33],'#95d1ba'),Edge(nodes[10],nodes[14],pheromone, paths[34],'#f9c114'),Edge(nodes[12],nodes[14],pheromone, paths[35],'#a8a8a8'),
         Edge(nodes[12],nodes[22],pheromone, paths[36],'#d55893'),Edge(nodes[21],nodes[22],pheromone, paths[37],'#8b543f'),Edge(nodes[14],nodes[22],pheromone, paths[38],'#f9c114'),
         Edge(nodes[20],nodes[23],pheromone, paths[39],'#03913e'), Edge(nodes[21],nodes[23],pheromone, paths[40],'#95d1ba')]

edges_df = pd.DataFrame(edges, index = paths, columns = ["edges"])