from manim import *
import math


def get_angle(g, a):
    h = math.sqrt((pow(g, 2) + pow(a, 2)))
    return -math.acos(a / h) + PI


def get_angle_negative(g, a):
    h = math.sqrt((pow(g, 2) + pow(a, 2)))
    return math.acos(a / h) + PI


class S0(Scene):
    def construct(self):
        title = Title("Backpropagation")
        self.add(title)
        self.wait(1)

        # ------------------------------------
        ziel = Tex("Ziel: Parameter finden, die die Kostenfunktion minimieren").shift(UP * 1.5).scale(1)
        ziel2 = Tex(r"$\rightarrow$ Gradient (Steigung) der einzelnen Parameter berechnen").scale(1).next_to(ziel,
                                                                                                             DOWN * 1.5)

        self.add(ziel, ziel2)

        self.wait(1)

        cost_derivative = MathTex(r"\frac{\partial C}{\partial w}").scale(1.5).shift(DOWN * 1.5)
        cost_derivative[0][:2].set_color(RED)
        cost_derivative[0][3:5].set_color(YELLOW)

        self.add(cost_derivative)

        self.wait(1)

        # jetzt ein paar definitionen

        self.remove(ziel, ziel2, cost_derivative)

        cost = MathTex(r"C \rightarrow Fehler", color=RED).scale(1).shift(UP * 1.5)
        net_input = MathTex(r"net_i^L \rightarrow Netzeingabe\:von\:Neuron\:i\:in\:Layer\:L", color=GREEN).scale(
            1).next_to(cost, DOWN * 1.5)
        output = MathTex(r"a_i^L \rightarrow Ausgabe\:von\:Neuron\:i\:in\:Layer\:L", color=BLUE).scale(1).next_to(
            net_input, DOWN * 1.5)
        activation_function = MathTex(r"\sigma \rightarrow Aktivierungsfunktion").scale(1).next_to(output, DOWN * 1.5)
        weight = MathTex(r"w_{ij}^L \rightarrow Gewicht\:von\:Neuron\:i\:zu\:Neuron\:j\:in\:Layer\:L",
                         color=YELLOW).scale(1).next_to(activation_function, DOWN * 1.5)

        self.add(cost, net_input, output, activation_function, weight)

        self.wait(1)

        self.remove(cost, net_input, output, activation_function, weight)

        # ------------------------------------
        LINE_THICKNESS = 5
        sum_body = Circle(stroke_width=LINE_THICKNESS).scale(0.8).set_color(GREEN)
        sum_tex = Tex(r"$\sum$").scale(1.3)
        sum_group = Group(sum_tex, sum_body)
        phi_body = Square(stroke_width=LINE_THICKNESS).scale(0.6).set_color(BLUE)
        phi_tex = Tex(r"$\sigma$").scale(1.4)
        phi_group = Group(phi_tex, phi_body)
        phi_group.shift(RIGHT * 4)
        phi_arrow = Arrow(start=sum_body.get_right(), end=phi_body.get_left(), buff=0, stroke_width=LINE_THICKNESS,
                          tip_length=0.3)
        phi_arrow_tex = Tex(r"$net_{i}^L$").set_color(GREEN)
        phi_arrow_tex.next_to(phi_arrow, UP, buff=0)
        phi_arrow_group = Group(phi_arrow, phi_arrow_tex)
        out_arrow = Arrow(start=phi_body.get_right(), end=phi_body.get_right() + RIGHT * 1.5, buff=0,
                          stroke_width=LINE_THICKNESS,
                          tip_length=0.3)
        out_arrow_tex = Tex(r"$o_{i}^L$").next_to(out_arrow, UP, buff=0).set_color(BLUE)
        out_arrow_group = Group(out_arrow, out_arrow_tex)
        weight_group = Group()
        weight_1_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_1_body_tex = Tex(r"$w_{1j}^L$")
        weight_1_group = Group(weight_1_body, weight_1_body_tex).shift(LEFT * 3)
        weight_1_group.shift(UP * 2.5)
        weight_1_arrow = Arrow(start=weight_1_body.get_right(), end=sum_body.point_at_angle(get_angle(2.5, 3)),
                               stroke_width=LINE_THICKNESS, tip_length=0.3, buff=0)
        weight_1_group.add(weight_1_arrow)

        weight_2_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_2_body_tex = Tex(r"$w_{2j}^L$")
        weight_2_group = Group(weight_2_body, weight_2_body_tex).shift(LEFT * 3)
        weight_2_group.shift(UP * 1)
        weight_2_arrow = Arrow(start=weight_2_body.get_right(), end=sum_body.point_at_angle(get_angle(1, 3)),
                               stroke_width=LINE_THICKNESS, tip_length=0.3, buff=0)
        weight_2_group.add(weight_2_arrow)

        weight_3_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_3_body_tex = Tex(r"$w_{3j}^L$")
        weight_3_group = Group(weight_3_body, weight_3_body_tex).shift(LEFT * 3).shift(DOWN * 0.5)
        weight_3_arrow = Arrow(start=weight_3_body.get_right(),
                               end=sum_body.point_at_angle(get_angle_negative(-0.5, 3)),
                               stroke_width=LINE_THICKNESS, buff=0,
                               tip_length=0.3)
        weight_3_group.add(weight_3_arrow)

        weight_n = MathTex(r"\vdots").shift(LEFT * 3)
        weight_n.shift(DOWN * 1.5)

        weight_i_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_i_body_tex = Tex(r"$w_{ij}^L$")
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

        self.add(neuron_group.scale(0.9).center().shift(DOWN * 0.5))

        self.wait(1)

        neuron_group.center()

        net_calc = MathTex(r"net_{i}^0 = \sum_{k=1}^{n} w_{kj}^0 x_{k}").shift(DOWN * 2 + RIGHT * 2).scale(1.2)
        net_calc[0][:5].set_color(GREEN)
        net_calc[0][11:15].set_color(YELLOW)

        n_explanation = Tex(r"n $\rightarrow$ Anzahl der Eingaben").next_to(net_calc, DOWN)

        # Layer 0 -> Eingaben sind eingaben und nicht Ausgaben von andren neuronen

        self.add(net_calc, n_explanation)

        self.wait(1)

        # aber man verbindet neuronen miteinander -> Eingaben sind outputs von andren neuronen

        self.clear()
        self.add(title)

        sum_body = Circle(stroke_width=LINE_THICKNESS).scale(0.8).set_color(GREEN)
        sum_tex = Tex(r"$\sum$").scale(1.3)
        sum_group = Group(sum_tex, sum_body)
        phi_body = Square(stroke_width=LINE_THICKNESS).scale(0.6).set_color(BLUE)
        phi_tex = Tex(r"$\sigma$").scale(1.4)
        phi_group = Group(phi_tex, phi_body)
        phi_group.shift(RIGHT * 4)
        phi_arrow = Arrow(start=sum_body.get_right(), end=phi_body.get_left(), buff=0, stroke_width=LINE_THICKNESS,
                          tip_length=0.3)
        phi_arrow_tex = Tex(r"$net_{i}^L$").set_color(GREEN)
        phi_arrow_tex.next_to(phi_arrow, UP, buff=0)
        phi_arrow_group = Group(phi_arrow, phi_arrow_tex)
        out_arrow = Arrow(start=phi_body.get_right(), end=phi_body.get_right() + RIGHT * 1.5, buff=0,
                          stroke_width=LINE_THICKNESS,
                          tip_length=0.3)
        out_arrow_tex = Tex(r"$o_{i}^L$").next_to(out_arrow, UP, buff=0).set_color(BLUE)
        out_arrow_group = Group(out_arrow, out_arrow_tex)
        weight_group = Group()
        weight_1_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_1_body_tex = Tex(r"$w_{1j}^L$")
        weight_1_group = Group(weight_1_body, weight_1_body_tex).shift(LEFT * 3)
        weight_1_group.shift(UP * 2.5)
        weight_1_arrow = Arrow(start=weight_1_body.get_right(), end=sum_body.point_at_angle(get_angle(2.5, 3)),
                               stroke_width=LINE_THICKNESS, tip_length=0.3, buff=0)
        weight_1_group.add(weight_1_arrow)

        weight_2_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_2_body_tex = Tex(r"$w_{2j}^L$")
        weight_2_group = Group(weight_2_body, weight_2_body_tex).shift(LEFT * 3)
        weight_2_group.shift(UP * 1)
        weight_2_arrow = Arrow(start=weight_2_body.get_right(), end=sum_body.point_at_angle(get_angle(1, 3)),
                               stroke_width=LINE_THICKNESS, tip_length=0.3, buff=0)
        weight_2_group.add(weight_2_arrow)

        weight_3_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_3_body_tex = Tex(r"$w_{3j}^L$")
        weight_3_group = Group(weight_3_body, weight_3_body_tex).shift(LEFT * 3).shift(DOWN * 0.5)
        weight_3_arrow = Arrow(start=weight_3_body.get_right(),
                               end=sum_body.point_at_angle(get_angle_negative(-0.5, 3)),
                               stroke_width=LINE_THICKNESS, buff=0,
                               tip_length=0.3)
        weight_3_group.add(weight_3_arrow)

        weight_n = MathTex(r"\vdots").shift(LEFT * 3)
        weight_n.shift(DOWN * 1.5)

        weight_i_body = Circle(stroke_width=LINE_THICKNESS).scale(0.5).set_color(YELLOW)
        weight_i_body_tex = Tex(r"$w_{ij}^L$")
        weight_i_group = Group(weight_i_body, weight_i_body_tex).shift(LEFT * 3).shift(DOWN * 2.5)
        weight_i_arrow = Arrow(start=weight_i_body.get_right(),
                               end=sum_body.point_at_angle(get_angle_negative(-2.5, 3)),
                               stroke_width=LINE_THICKNESS, buff=0,
                               tip_length=0.3)
        weight_i_group.add(weight_i_arrow)

        input_group = Group()

        input_1_tex = Tex(r"$o_{1}^{L-1}$", color=BLUE).shift(UP * 2.5).shift(LEFT * 5)
        input_1_arrow = Arrow(start=input_1_tex.get_right() + RIGHT * 0.1, end=weight_1_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_1_tex, input_1_arrow)

        input_2_tex = Tex(r"$o_{2}^{L-1}$", color=BLUE).shift(UP * 1).shift(LEFT * 5)
        input_2_arrow = Arrow(start=input_2_tex.get_right() + RIGHT * 0.1, end=weight_2_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_2_tex, input_2_arrow)

        input_3_tex = Tex(r"$o_{3}^{L-1}$", color=BLUE).shift(LEFT * 5).shift(DOWN * 0.5)
        input_3_arrow = Arrow(start=input_3_tex.get_right() + RIGHT * 0.1, end=weight_3_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_3_tex, input_3_arrow)

        input_i_tex = Tex(r"$o_{i}^{L-1}$", color=BLUE).shift(DOWN * 2.5).shift(LEFT * 5)
        input_i_arrow = Arrow(start=input_i_tex.get_right() + RIGHT * 0.1, end=weight_i_body.get_left(),
                              stroke_width=LINE_THICKNESS, buff=0,
                              tip_length=0.3)

        input_group.add(input_i_tex, input_i_arrow)

        input_n = MathTex(r"\vdots").shift(LEFT * 5)
        input_n.shift(DOWN * 1.5)
        input_group.add(input_n)

        weight_group.add(weight_1_group, weight_2_group, weight_3_group, weight_n, weight_i_group)
        neuron_group = Group(sum_group, phi_group, phi_arrow_group, out_arrow_group, weight_group, input_group)

        self.add(neuron_group.scale(0.9).center())

        net_calc = MathTex(r"net_{i}^L = \sum_{k=1}^{n} w_{kj}^L o_{k}^{L-1}").shift(DOWN * 2 + RIGHT * 2).scale(1.2)
        net_calc[0][:5].set_color(GREEN)
        net_calc[0][11:15].set_color(YELLOW)
        net_calc[0][15:20].set_color(BLUE)

        n_explanation = Tex(r"n $\rightarrow$ Anzahl der Neuronen in Layer L - 1").next_to(net_calc, DOWN)

        self.add(net_calc, n_explanation)
        self.wait(1)

        self.remove(net_calc, n_explanation)

        out_calc = MathTex(r"o_{i}^L = \sigma(net_{i}^L)").shift(DOWN * 2 + RIGHT * 2).scale(1.2)

        out_calc[0][:3].set_color(BLUE)
        out_calc[0][6:11].set_color(GREEN)

        self.add(out_calc)

        self.wait(1)

        self.clear()
        self.add(title)

        cost_calc = MathTex(r"C = \frac{1}{2} \sum_{i=1}^{n} (o_{i}^{L_{-1}} - t_i)^2").scale(1.2).shift(
            RIGHT * 2.5 + UP * 1)

        cost_calc[0][0].set_color(RED)
        cost_calc[0][11:16].set_color(BLUE)
        cost_calc[0][17:19].set_color(GREEN)

        self.add(cost_calc)

        output_values = [0.6, 0.2, 0.8, 0.3]
        outputs = Group()
        for i in range(3, -1, -1):
            outputs.add(Group(Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=output_values[i]),
                              MathTex("o_{" + (str(i + 1) if i != 3 else "i") + "}^{L_{-1}}").scale(0.7)))

        outputs.arrange(UP, buff=0.3).shift(LEFT * 6 + DOWN * 0.5)

        self.add(outputs)

        self.wait(1)

        target_values = [0.2, 0.7, 0.6, 0.4]
        targets = Group()
        for i in range(3, -1, -1):
            targets.add(Group(Circle(radius=0.5, color=GREEN, fill_color=GREEN, fill_opacity=target_values[i]),
                              MathTex("t_{" + (str(i + 1) if i != 3 else "i") + "}").scale(0.7)))

        targets.arrange(UP, buff=0.3).shift(LEFT * 4 + DOWN * 0.5)

        equals = MathTex("=").scale(1.5).next_to(targets, RIGHT)
        minus = MathTex("-").scale(1.5).next_to(outputs, RIGHT)

        self.add(targets, minus)

        self.wait(1)

        error_values = [0.4, 0.5, 0.2, 0.1]
        errors = Group()
        for i in range(3, -1, -1):
            errors.add(Group(Circle(radius=0.5, color=RED, fill_color=RED, fill_opacity=error_values[i]),
                             MathTex("e_{" + (str(i + 1) if i != 3 else "i") + "}").scale(0.7)))
        errors.arrange(UP, buff=0.3).shift(LEFT * 2 + DOWN * 0.5)

        self.add(errors, equals)

        self.wait(1)

        errors_brace = Brace(errors, direction=RIGHT)

        final_error = Group(Circle(radius=0.7, color=RED, fill_color=RED, fill_opacity=0.5), MathTex("C").scale(0.7))
        final_error.next_to(errors_brace, RIGHT)

        self.add(errors_brace, final_error)

        self.wait(1)

        self.clear()

