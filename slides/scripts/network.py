import warnings

from manim import *
import math

LINE_THICKNESS = 2
STRUCTURE = [2, 4, 4, 2]


class Scene(ThreeDScene):
    def construct(self):
        neurons_Group = Group()
        for i in range(len(STRUCTURE)):
            group = Group()
            for j in range(STRUCTURE[i]):
                group.add(
                    Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=YELLOW).shift(
                        UP * (j - STRUCTURE[i] / 2 + 0.5)))
            group.shift(RIGHT * (i - len(STRUCTURE) / 2) * 3)
            neurons_Group.add(group)
        weights_group = Group()
        for i in range(len(STRUCTURE) - 1):
            for j in range(STRUCTURE[i]):
                for k in range(STRUCTURE[i + 1]):
                    weights_group.add(
                        Line(stroke_width=LINE_THICKNESS, start=neurons_Group[i][j].get_right(),
                             end=neurons_Group[i + 1][k].get_left()))
        neurons_Group[0].set_color(RED)
        neurons_Group[-1].set_color(BLUE)

        network_group = Group(neurons_Group, weights_group).arrange(ORIGIN).shift(DOWN*0.6)
        self.add(Text("Input\nLayer").to_edge(UP).set_x(neurons_Group[0].get_x()).set_color(RED))
        self.add(Text("Hidden\nLayers").to_edge(UP).set_x(
            (neurons_Group[1].get_x() + neurons_Group[2].get_x()) / 2).set_color(YELLOW))
        self.add(Text("Ouput\nLayer").to_edge(UP).set_x(neurons_Group[-1].get_x()).set_color(BLUE))
        self.add(network_group)
        self.wait(1)

