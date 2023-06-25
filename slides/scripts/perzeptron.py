from manim import *
import math

LINE_THICKNESS = 3


def get_angle(g, a):
    h = math.sqrt((pow(g, 2) + pow(a, 2)))
    return -math.acos(a / h) + PI


def get_angle_negative(g, a):
    h = math.sqrt((pow(g, 2) + pow(a, 2)))
    return math.acos(a / h) + PI


class S0(Scene):
    def construct(self):
        sum_body = Circle(stroke_width=LINE_THICKNESS).scale(0.8).set_color(GREEN)
        sum_tex = Tex(r"$\sum$").scale(1.3)
        sum_group = Group(sum_tex, sum_body)
        phi_body = Square(stroke_width=LINE_THICKNESS).scale(0.6).set_color(BLUE)
        phi_tex = Tex(r"$\varphi$").scale(1.4)
        phi_group = Group(phi_tex, phi_body)
        phi_group.shift(RIGHT * 4)
        phi_arrow = Arrow(start=sum_body.get_right(), end=phi_body.get_left(), buff=0, stroke_width=LINE_THICKNESS,
                          tip_length=0.3)
        phi_arrow_tex = Tex(r"$net_{j}$").set_color(GREEN)
        phi_arrow_tex.next_to(phi_arrow, UP, buff=0)
        phi_arrow_group = Group(phi_arrow, phi_arrow_tex)
        out_arrow = Arrow(start=phi_body.get_right(), end=phi_body.get_right() + RIGHT * 1.5, buff=0,
                          stroke_width=LINE_THICKNESS,
                          tip_length=0.3)
        out_arrow_tex = Tex(r"$o_{j}$").next_to(out_arrow, UP, buff=0).set_color(BLUE)
        out_arrow_group = Group(out_arrow, out_arrow_tex)
        weight_group = Group()
        weight_1_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_1_body_tex = Tex(r"$w_{1j}$")
        weight_1_group = Group(weight_1_body, weight_1_body_tex).shift(LEFT * 3)
        weight_1_group.shift(UP * 2.5)
        weight_1_arrow = Arrow(start=weight_1_body.get_right(), end=sum_body.point_at_angle(get_angle(2.5, 3)),
                               stroke_width=LINE_THICKNESS, tip_length=0.3, buff=0)
        weight_1_group.add(weight_1_arrow)

        weight_2_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_2_body_tex = Tex(r"$w_{2j}$")
        weight_2_group = Group(weight_2_body, weight_2_body_tex).shift(LEFT * 3)
        weight_2_group.shift(UP * 1)
        weight_2_arrow = Arrow(start=weight_2_body.get_right(), end=sum_body.point_at_angle(get_angle(1, 3)),
                               stroke_width=LINE_THICKNESS, tip_length=0.3, buff=0)
        weight_2_group.add(weight_2_arrow)

        weight_3_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_3_body_tex = Tex(r"$w_{3j}$")
        weight_3_group = Group(weight_3_body, weight_3_body_tex).shift(LEFT * 3).shift(DOWN * 0.5)
        weight_3_arrow = Arrow(start=weight_3_body.get_right(),
                               end=sum_body.point_at_angle(get_angle_negative(-0.5, 3)),
                               stroke_width=LINE_THICKNESS, buff=0,
                               tip_length=0.3)
        weight_3_group.add(weight_3_arrow)

        weight_n = MathTex(r"\vdots").shift(LEFT * 3)
        weight_n.shift(DOWN * 1.5)

        weight_i_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_i_body_tex = Tex(r"$w_{ij}$")
        weight_i_group = Group(weight_i_body, weight_i_body_tex).shift(LEFT * 3).shift(DOWN * 2.5)
        weight_i_arrow = Arrow(start=weight_i_body.get_right(),
                               end=sum_body.point_at_angle(get_angle_negative(-2.5, 3)),
                               stroke_width=LINE_THICKNESS, buff=0,
                               tip_length=0.3)
        weight_i_group.add(weight_i_arrow)

        input_group = Group()

        input_1_tex = Tex(r"$x_{1}$").shift(UP * 2.5).shift(LEFT * 5)
        input_1_arrow = Arrow(start=input_1_tex.get_right() + RIGHT * 0.1, end=weight_1_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_1_tex, input_1_arrow)

        input_2_tex = Tex(r"$x_{2}$").shift(UP * 1).shift(LEFT * 5)
        input_2_arrow = Arrow(start=input_2_tex.get_right() + RIGHT * 0.1, end=weight_2_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_2_tex, input_2_arrow)

        input_3_tex = Tex(r"$x_{3}$").shift(LEFT * 5).shift(DOWN * 0.5)
        input_3_arrow = Arrow(start=input_3_tex.get_right() + RIGHT * 0.1, end=weight_3_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_3_tex, input_3_arrow)

        input_i_tex = Tex(r"$x_{i}$").shift(DOWN * 2.5).shift(LEFT * 5)
        input_i_arrow = Arrow(start=input_i_tex.get_right() + RIGHT * 0.1, end=weight_i_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_i_tex, input_i_arrow)

        input_n = MathTex(r"\vdots").shift(LEFT * 5)
        input_n.shift(DOWN * 1.5)
        input_group.add(input_n)

        weight_group.add(weight_1_group, weight_2_group, weight_3_group, weight_n, weight_i_group)
        neuron_group = Group(sum_group, phi_group, phi_arrow_group, out_arrow_group, weight_group, input_group)

        self.add(neuron_group.shift(DOWN * 0.5).scale(0.9))

        # ------------------------------------

        title = Title("Perzeptron")
        self.add(title)

        self.wait(1)

        neuron_group.scale(0.7).shift(LEFT * 3).shift(UP * 1)

        Netzeingabe = Tex(r"Netzeingabe: ")
        Netzeingabe_formel = MathTex(r"net_j = \sum_{i=1}^{n} w_{ij} \cdot x_i")
        Netzeingabe_formel[0][0:4].set_color(GREEN)
        Netzeingabe_formel[0][10:13].set_color(YELLOW)

        self.add(Netzeingabe.shift(DOWN * 1))
        self.add(Netzeingabe_formel.next_to(Netzeingabe, RIGHT))

        self.wait(1)

        Ausgabe = Tex(r"Ausgabe: ")
        Ausgabe_formel = MathTex(r"o_j = \varphi(net_j)")
        Ausgabe_formel[0][0:2].set_color(BLUE)
        Ausgabe_formel[0][5:9].set_color(GREEN)

        self.add(Ausgabe.shift(DOWN * 2.5))
        self.add(Ausgabe_formel.next_to(Ausgabe, RIGHT))

        self.wait(1)

        # hide everything and display a sigmoid function
        main_group = Group(neuron_group, Netzeingabe, Netzeingabe_formel, Ausgabe, Ausgabe_formel)
        main_group.shift(LEFT * 15)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-0.25, 1.5, 0.5],
            x_length=10,
            y_length=5,
            x_axis_config={"numbers_to_include": [-1, -2, 2, 1]},
            y_axis_config={"numbers_to_include": [1, 0.5]},
        ).shift(DOWN * 1)

        plt = axes.plot(lambda x: 1 / (1 + np.exp(-x)), x_range=[-4, 4], color=BLUE)
        self.add(plt)
        self.add(axes)

        self.wait(1)

        # sigmoid derivative
        plt2 = axes.plot(lambda x: (1 / (1 + np.exp(-x))) * (1 - (1 / (1 + np.exp(-x)))), x_range=[-4, 4], color=RED)
        self.add(plt2)

        self.wait(1)

        self.remove(axes, plt, plt2)
        main_group.shift(RIGHT * 15)

        self.wait(1)
