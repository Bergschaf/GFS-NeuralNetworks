from manim import *


def get_gradient(func, x, h=0.0001):
    return (func(x + h) - func(x - h)) / (2 * h)


class S0(Scene):

    def construct(self):
        title = Title("Wie lernen Neuronale Netzwerke?")

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=5).shift(DOWN * 0.5)
        # -1 / ((x - 5) ** 2 + 1) + 2
        spike = lambda x, y: lambda xx: -y / ((xx - x) ** 2 + 1)
        # plt = axes.plot(lambda x: spike(2,2)(x) + 2 + spike(6, 1)(x) - spike(-0.5, 3)(x) - spike(11, 4)(x), x_range=[0, 10], color=BLUE)
        func = lambda x: -((-1 / 9.5 * (x - 3.2) ** 4) * 1.5 - (1 / 3 * (x - 3.22) ** 3) * 1.3 - 1.3) + spike(7, 2)(
            x * 2) * 0.3
        plt = axes.plot(func, x_range=[0, 4.8], color=BLUE)

        self.add(plt, axes, title)

        x_label = Tex(r"Parameter x").next_to(axes, DOWN).shift(RIGHT * 3)
        y_label = MathTex(r"C(x)").next_to(axes, LEFT).shift(UP * 2.5)

        self.add(x_label, y_label)

        self.wait(1)

        g = 1.11
        l = 3.485
        global_minimum = Dot(axes.c2p(g, func(g)), color=RED, radius=0.1)
        local_minimum = Dot(axes.c2p(l, func(l)), color=GREEN, radius=0.1)

        global_minimum_label = Text(r"globales Minimum", color=RED).next_to(global_minimum, DOWN * 0.3).scale(0.7)
        local_minimum_label = Text(r"lokales Minimum", color=GREEN).next_to(local_minimum, DOWN * 0.3).scale(0.7)

        self.add(global_minimum, local_minimum, global_minimum_label, local_minimum_label)

        self.wait(1)

        random_starting_point = Dot(axes.c2p(4.5, func(4.5)), color=YELLOW, radius=0.1)
        random_starting_point_label = Text("zufälliger\nStartpunkt", color=YELLOW).scale(0.7).next_to(
            random_starting_point, RIGHT * 1)

        self.add(random_starting_point, random_starting_point_label)

        self.wait(1)

        self.remove(random_starting_point_label)
        random_starting_point_label = MathTex(r"x_0", color=YELLOW).scale(1.3).next_to(
            random_starting_point, RIGHT * 1)

        self.add(random_starting_point_label)

        self.wait(1)

        grad_calc = MathTex(r"C'(x_0) = 3.71").scale(1.3)

        self.add(grad_calc)

        self.wait(1)

        gradient = get_gradient(func, 4.5)
        print(gradient)
        random_start_point_cords = random_starting_point.get_center()
        gradient_down_cords = axes.c2p(4.1, func(4.5) - gradient * 0.4)

        gradient_arrow = Arrow(random_start_point_cords, gradient_down_cords, color=RED, stroke_width=7,
                               max_stroke_width_to_length_ratio=1000)

        self.add(gradient_arrow)

        self.wait(1)

        grad_calc.shift(UP * 1)

        new_x_calc = MathTex(r"x_1 = x_0 - \eta \cdot C'(x_0)").scale(1.3).next_to(grad_calc, DOWN * 2.5)
        # hier lernrate n erklären

        self.add(new_x_calc)

        self.wait(1)

        x_1_x_pos = 4.05
        x_1_y_pos = func(x_1_x_pos)

        x_1 = Dot(axes.c2p(x_1_x_pos, x_1_y_pos), color=YELLOW, radius=0.1)
        x_1_label = MathTex(r"x_1", color=YELLOW).scale(1.3).next_to(x_1, RIGHT * 1)

        self.add(x_1, x_1_label)

        self.wait(1)

        self.remove(grad_calc, new_x_calc)

        gradient = get_gradient(func, x_1_x_pos)
        print(gradient)

        grad_calc = MathTex(r"C'(x_1) = 1.82").scale(1.3).shift(UP * 1)

        self.add(grad_calc)

        self.wait(1)

        gradient_arrow_2 = Arrow(x_1.get_center(), axes.c2p(x_1_x_pos - 0.4, x_1_y_pos - gradient * 0.4), color=RED,
                                    stroke_width=4, max_stroke_width_to_length_ratio=1000)

        self.add(gradient_arrow_2)

        self.wait(1)

        new_x_calc = MathTex(r"x_2 = x_1 - \eta \cdot C'(x_1)").scale(1.3).next_to(grad_calc, DOWN * 2.5)

        self.add(new_x_calc)

        x_2 = Dot(axes.c2p(3.7, func(3.7)), color=YELLOW, radius=0.1)
        x_2_label = MathTex(r"x_2", color=YELLOW).scale(1.3).next_to(x_2, RIGHT * 1)

        self.add(x_2, x_2_label)

        self.wait(1)

