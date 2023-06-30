from manim import *


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
        plt = axes.plot(
            lambda x: -((-1 / 9.5 * (x - 3.2) ** 4) * 1.5 - (1 / 3 * (x - 3.22) ** 3) * 1.3 - 1.3) + spike(7, 2)(
                x * 2) * 0.3, x_range=[0, 4.8], color=BLUE)

        self.add(plt, axes, title)

        self.wait(1)
