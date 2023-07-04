from manim import *


class S0(Scene):
    def construct(self):
        title = Title("Neuronale Netwerke")
        self.add(title)

        self.wait(1)

        img1 = ImageMobject("assets/DALLE.png").scale(0.7).shift(LEFT * 3.85).shift(DOWN * 0.5)
        img2 = ImageMobject("assets/BERG.png").scale(0.7).next_to(img1, RIGHT * 2.5)

        self.add(img1)
        self.add(img2)

        self.wait(1)
