import warnings

from manim import *
import math
import random

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

        self.remove(title)

        title = Title("Wie lernen Neuronale Netze?")
        self.add(title)

        self.wait(1)

        self.remove(network_group, text_group)

        inputs = Group()
        i1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED)
        i2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=RED).next_to(i1, RIGHT * 0.5)
        inputs.add(Group(i1, i2))

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
        inputs.center().shift(UP * 1.5)

        outputs = Group()
        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=1, fill_color=BLUE)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=1, fill_color=BLUE).next_to(c1,
                                                                                                                  RIGHT * 0.5)

        outputs.add(Group(c1, c2).next_to(inputs[0], DOWN * 10))

        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=0, fill_color=BLUE)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=1, fill_color=BLUE).next_to(c1,
                                                                                                                  RIGHT * 0.5)

        outputs.add(Group(c1, c2).next_to(inputs[1], DOWN * 10))

        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=1, fill_color=BLUE)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=0, fill_color=BLUE).next_to(c1,
                                                                                                                  RIGHT * 0.5)
        outputs.add(Group(c1, c2).next_to(inputs[2], DOWN * 10))

        c1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE)
        c2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE).next_to(c1, RIGHT * 0.5)
        outputs.add(Group(c1, c2).next_to(inputs[3], DOWN * 10))

        arrows = Group()
        for i in range(4):
            arrows.add(Arrow(inputs[i].get_bottom() + DOWN * 0.2, outputs[i].get_top() + UP * 0.2,
                             stroke_width=LINE_THICKNESS * 2))

        self.add(inputs, outputs, arrows)

        self.wait(1)

        self.clear()
        self.add(title)

        # set the weights to random colors between blue and red
        for weight in weights_group:
            weight.set_color(interpolate_color(WHITE, GREY_D, random.random()))

        self.add(network_group.shift(UP * 0.9))

        self.wait(1)

        network_group.scale(0.8)

        input1 = i1.copy().set_opacity(1)
        input2 = i2.copy().next_to(input1, RIGHT * 0.5)
        right_input_group = Group(input1, input2).next_to(network_group, LEFT * 4).scale(0.8)

        input_brace = Brace(right_input_group, RIGHT).scale(1.2).shift(RIGHT * 0.2)

        self.add(right_input_group, input_brace)

        neurons_Group[0][1].set_opacity(1)

        output1 = c1.copy().set_opacity(0.3)
        output2 = c2.copy().next_to(output1, RIGHT * 0.5).set_opacity(0.7)
        right_output_group = Group(output1, output2).next_to(network_group, RIGHT * 4).scale(0.8)

        output_brace = Brace(right_output_group, LEFT).scale(1.2).shift(LEFT * 0.2)

        self.add(right_output_group, output_brace)

        neurons_Group[-1][1].set_opacity(0.3)
        neurons_Group[-1][0].set_opacity(0.7)

        for ng in neurons_Group[1:-1]:
            for neuron in ng:
                neuron.set_opacity(random.random() * 0.7 + 0.3)
                neuron.set_color(YELLOW)

        self.wait(1)

        self.clear()
        self.add(title)

        RANDOM_OUTPUTS = {(0, 0): (0.3, 0.7), (0, 1): (0.9, 0.6), (1, 0): (0.6, 0.3), (1, 1): (0.4, 0.5)}
        random_outputs = Group()
        for id, i in enumerate(RANDOM_OUTPUTS):
            r1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=RANDOM_OUTPUTS[i][0],
                        fill_color=BLUE)
            r2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=BLUE, fill_opacity=RANDOM_OUTPUTS[i][1],
                        fill_color=BLUE).next_to(r1, RIGHT * 0.5)
            random_outputs.add(Group(r1, r2).next_to(inputs[id], DOWN * 5))

        self.add(random_outputs.shift(RIGHT * 1), inputs.shift(RIGHT * 1), outputs.shift(RIGHT * 1))

        inputs_text = Text("Eingabe").scale(0.8)
        expected_outputs_text = Text("Ziel").scale(0.8)
        random_outputs_text = Text("Ausgabe").scale(0.8)
        x = 5.5
        inputs_text.shift(LEFT * x).set_y(inputs.get_y())
        expected_outputs_text.shift(LEFT * x).set_y(outputs.get_y())
        random_outputs_text.shift(LEFT * x).set_y(random_outputs.get_y())

        self.add(inputs_text, expected_outputs_text, random_outputs_text)

        self.wait(1)

        x2 = 0.3
        expected_outputs_text.shift(UP * x2)
        random_outputs_text.shift(UP * x2)
        outputs.shift(UP * x2)
        random_outputs.shift(UP * x2)

        # line below the outputs group
        fancy_line = Line(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=LINE_THICKNESS * 2).next_to(outputs,
                                                                                                     DOWN * 1.5)

        self.add(fancy_line)

        ERRORS = [(0.7, 0.3), (0.9, 0.4), (0.4, 0.3), (0.4, 0.5)]
        errors = Group()
        for i in range(4):
            e1 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=GREEN, fill_opacity=ERRORS[i][0],
                        fill_color=GREEN)
            e2 = Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=GREEN, fill_opacity=ERRORS[i][1],
                        fill_color=GREEN).next_to(e1, RIGHT * 0.5)
            errors.add(Group(e1, e2).next_to(outputs[i], DOWN * 3))

        self.add(errors)

        errors_text = Text("Fehler").scale(0.8)
        errors_text.shift(LEFT * x).set_y(errors.get_y())

        self.add(errors_text)

        self.wait(1)

        self.clear()
        title = Title("Neuronale Netzwerke als Funktionen")
        self.add(title)

        function = MathTex("N(inputs) = outputs").scale(1.5)
        function[0][0].set_color(YELLOW)
        #function[0][2:8].set_color(RED)
        function[0][10:17].set_color(BLUE)

        self.add(function)

        self.wait(1)

        self.remove(function)
        cost_function = MathTex("C(Gewichte) = Fehlerwert").scale(1.5)
        cost_function[0][0].set_color(RED)
        cost_function[0][2:10].set_color(YELLOW)

        self.add(cost_function)

        self.wait(1)

        self.remove(cost_function)

        cost_function = MathTex("C(w_{1}, w_{2}, w_{3}, ... ,w_{i}) = Fehlerwert").scale(1.5)

        cost_function[0][0].set_color(RED)
        cost_function[0][2:4].set_color(YELLOW)
        cost_function[0][5:7].set_color(YELLOW)
        cost_function[0][8:10].set_color(YELLOW)
        cost_function[0][15:17].set_color(YELLOW)

        self.add(cost_function)

        self.wait(1)