import sys
import pandas as pd
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont
from PyQt5.QtCore import Qt, QPoint
from data import nodes, edges_df, nodes_name, pheromone, edges
from Aco import Aco


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("window/map.ui", self)
        self.setWindowTitle("Metro CDMX")
        self.setGeometry(0, 0, 1544, 1150)
        self.flag = False
        self.route = []
        self.draw_labels()
        self.optimal_route_name = 0
        self.create_route.clicked.connect(self.get_nodes)
        self.show()

    def draw_labels(self):
        for node in nodes:
            label_round = QLabel(node.get_name(), self)
            label_round.move(node.get_position()[0]+10, node.get_position()[1] - 30)
            label_round.setFont(QFont('Arial', 8))
            self.start_node.addItem(node.get_name())
            self.end_node.addItem(node.get_name())

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(7)
        des = [5, 5]
        for _, edge in edges_df.iterrows():
            pen.setColor(QtGui.QColor(edge['edges'].get_color()))
            painter.setPen(pen)
            painter.drawLine(
                QPoint(edge['edges'].get_node1().get_position()[0] + des[0],
                       edge['edges'].get_node1().get_position()[1] + des[1]),
                QPoint(edge['edges'].get_node2().get_position()[0] + des[0],
                       edge['edges'].get_node2().get_position()[1] + des[1])
            )
        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))

        for node in nodes:
            x = node.get_position()[0]
            y = node.get_position()[1]
            painter.drawEllipse(x, y, 12, 12)

        if self.flag:
            for r in range(len(self.route[0])):
                print(self.route[0][r])
                pen.setColor(QtGui.QColor("#25ff00"))
                painter.setPen(pen)
                painter.drawLine(
                    QPoint(self.route[0][r].get_node1().get_position()[0] + des[0],
                           self.route[0][r].get_node1().get_position()[1] + des[1]),
                    QPoint(self.route[0][r].get_node2().get_position()[0] + des[0],
                           self.route[0][r].get_node2().get_position()[1] + des[1])
                )

            painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            for node in nodes:
                x = node.get_position()[0]
                y = node.get_position()[1]
                painter.drawEllipse(x, y, 12, 12)

            movement = 35
            painter_text = QPainter(self)
            font = painter_text.font()
            font.setPixelSize(28)
            painter_text.setFont(font)
            painter_text.drawText(1250,100, "Best route: ")
            for l in range(len(self.optimal_route_name.values.tolist())):
                painter_text.drawText(1250, 120+movement, self.optimal_route_name.values.tolist()[l][0])
                movement += 35

    def get_nodes(self) -> None:
        initial_node = nodes[nodes_name.index(self.start_node.currentText())]
        end_node = nodes[nodes_name.index(self.end_node.currentText())]
        self.route = main(initial_node, end_node)

        route_names = []
        for i in range(len(self.route[0])):
            print(self.route[0][i].get_name())
            route_names.extend(
                [self.route[0][i].get_node1().get_name(), self.route[0][i].get_node2().get_name()])
            self.optimal_route_name = pd.DataFrame(route_names).drop_duplicates()

        self.flag = True
        self.update()
        for edge in edges:
            edge.set_pheromone(pheromone)


def main(initial_node, end_node):
    epochs = 1

    ants = 10
    while epochs > 0:
        aco = Aco(0.5, 1, ants)
        routes = aco.get_trajectories(initial_node, end_node)
        aco.update_pheromone(routes)
        the_best_route = aco.get_best_route(routes)
        epochs = epochs - 1

    return the_best_route


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Gui_ = Gui()
    Gui_.show()
    sys.exit(app.exec_())
