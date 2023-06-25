import warnings

from manim import *
import math

LINE_THICKNESS = 2
STRUCTURE = [2, 4, 4, 2]


class Scene(ThreeDScene):
    def construct(self):
        title = Title("Netzwerk")
        self.add(title)

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

        network_group = Group(neurons_Group, weights_group).arrange(ORIGIN).shift(DOWN * 0.6)
        text_group = Group(Text("Input\nLayer").to_edge(UP).set_x(neurons_Group[0].get_x()).set_color(RED),
                           Text("Hidden\nLayers").to_edge(UP).set_x(
                               (neurons_Group[1].get_x() + neurons_Group[2].get_x()) / 2).set_color(YELLOW),
                           Text("Ouput\nLayer").to_edge(UP).set_x(neurons_Group[-1].get_x()).set_color(BLUE)
                           )

        self.add(network_group.shift(DOWN * 0.9))
        self.add(text_group.shift(DOWN * 1.5))
        self.wait(1)

        self.clear()
        title = Title("Wie lernen Neuronale Netze?")
        self.add(title)

        self.wait(1)

        inputs = Group()
        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED).next_to(c1, RIGHT * 0.5)
        inputs.add(Group(c1, c2))

        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED, fill_opacity=1, fill_color=RED)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED, fill_opacity=0, fill_color=RED).next_to(c1,
                                                                                                                RIGHT * 0.5)
        inputs.add(Group(c1, c2).next_to(inputs, RIGHT * 4))

        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED, fill_opacity=0, fill_color=RED)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED, fill_opacity=1, fill_color=RED).next_to(c1,
                                                                                                                RIGHT * 0.5)
        inputs.add(Group(c1, c2).next_to(inputs, RIGHT * 4))

        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED, fill_opacity=1, fill_color=RED)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED, fill_opacity=1, fill_color=RED).next_to(c1,
                                                                                                                RIGHT * 0.5)
        inputs.add(Group(c1, c2).next_to(inputs, RIGHT * 4))

        self.add(inputs.center().shift(UP * 1.5))

        self.wait(1)

        self.add(network_group.shift(UP * 0.9))

        self.wait(1)
