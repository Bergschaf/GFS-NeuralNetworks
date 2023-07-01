from manim import *
from PIL import Image
import os


class S0(Scene):
    def construct(self):
        title = Title("MNIST Datenset")
        self.add(title)

        imgs = []
        for i in range(10):
            img = ImageMobject(f"assets/example_{i}.png")
            imgs.append(img)
        imgs = Group(*imgs)
        imgs.arrange_in_grid(2, 5)
        imgs.scale(5)
        imgs.center()
        self.add(imgs)
        self.wait(1)
        self.remove(imgs)

        bullet_points = [
            "Bilder von handgeschriebenen Ziffern",
            "60.000 Trainingsbilder, 10.000 Testbilder",
            "28x28 Pixel, Graustufen",
            "10 Klassen (0-9)"]
        bullet_points = BulletedList(*bullet_points)
        self.add(bullet_points)
        self.wait(1)

        self.clear()
        title = Title("MNIST Datenset - Netzwerk")
        self.add(title)

        LINE_THICKNESS = 1
        STRUCTURE = [20, 16, 16, 10]
        neurons_Group = Group()
        for i in range(len(STRUCTURE)):
            group = Group()
            for j in range(STRUCTURE[i]):
                group.add(
                    Circle(radius=0.4, stroke_width=LINE_THICKNESS, color=YELLOW, fill_color=YELLOW,
                           fill_opacity=1).shift(
                        UP * (j - STRUCTURE[i] / 2 + 0.5)))
            group.shift(RIGHT * (i - len(STRUCTURE) / 2) * 7)
            neurons_Group.add(group)
        weights_group = Group()
        for i in range(len(STRUCTURE) - 1):
            for j in range(STRUCTURE[i]):
                if i == 0 and j >= 9 and j <= 11:
                    neurons_Group[i][j].scale(0.00001)
                    pass
                else:
                    for k in range(STRUCTURE[i + 1]):
                        weights_group.add(
                            Line(stroke_width=LINE_THICKNESS, start=neurons_Group[i][j].get_right(),
                                 end=neurons_Group[i + 1][k].get_left()))
        neurons_Group[0].set_color(RED)
        neurons_Group[-1].set_color(BLUE)

        network_group = Group(neurons_Group, weights_group).arrange(ORIGIN).shift(DOWN * 0.6)
        network_group.add(Text("...").next_to(neurons_Group[0][10], RIGHT).scale(2).shift(LEFT * 0.5 + DOWN * 0.2))
        self.add(network_group.scale(0.3))

        network_group.shift(DOWN * 0.25)

        label_784 = Text("784", color=RED).next_to(neurons_Group[0][-1], UP, buff=0.1).scale(0.7)
        label_16_1 = Text("16", color=YELLOW).next_to(neurons_Group[1][-1], UP, buff=0.1).scale(0.7)
        label_16_2 = Text("16", color=YELLOW).next_to(neurons_Group[2][-1], UP, buff=0.1).scale(0.7)
        label_10 = Text("10", color=BLUE).next_to(neurons_Group[3][-1], UP, buff=0.1).scale(0.7)

        self.add(label_784, label_16_1, label_16_2, label_10)

        self.wait(1)

        imgs = []
        for i in range(5):
            img = ImageMobject(f"assets/example_{i}.png")
            imgs.append(img)
        imgs = Group(*imgs)
        imgs.arrange_in_grid(5, 1).scale(2.5)
        self.add(imgs.next_to(network_group, LEFT, buff=1.2))

        left_brace = Brace(imgs, RIGHT)
        self.add(left_brace)

        self.wait(1)

        numbers = [7, 2, 1, 0, 4]
        for i in range(5):
            numbers.append(Text(str(numbers[i])))
        numbers = numbers[5:]
        numbers = Group(*numbers)
        numbers.arrange_in_grid(5, 1, buff=0.6).scale(0.8)
        self.add(numbers.next_to(network_group, RIGHT, buff=1.2))

        right_brace = Brace(numbers, LEFT)
        self.add(right_brace)

        self.wait(1)

