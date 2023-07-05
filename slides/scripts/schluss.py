from manim import *


class S0(Scene):
    def construct(self):
        title = Title("DALLE 2")

        # zum schluss noch wie dalle 2 funktioniert
        self.add(title)

        self.wait(1)

        img1 = ImageMobject("assets/DALLE_1.png").scale(0.4)
        img2 = ImageMobject("assets/DALLE_2.png").scale(0.4)
        img3 = ImageMobject("assets/DALLE_3.png").scale(0.4)
        img4 = ImageMobject("assets/DALLE_4.png").scale(0.4)

        img_group = Group(img1, img2, img3, img4).arrange_in_grid(2, 2).scale(0.9).shift(DOWN * 0.5)

        self.add(img_group)

        self.wait(1)

        self.remove(img_group)

        img_e = ImageMobject("assets/DALLE_E.png").shift(UP * 1).scale(1.3)

        bulleted_list = ["Text wird in ein Textembedding umgewandelt",
                         "Textembedding wird in ein Bildembedding umgewandelt",
                         "Bildembedding wird mit Diffusion in ein Bild umgewandelt", "Bild wird hochskaliert"]

        list = BulletedList(*bulleted_list).scale(0.8).shift(DOWN * 2.1).align_to(img_e, LEFT)

        self.add(list, img_e)

        self.wait(1)
        self.clear()

        title = Title("Noch Fragen?")
        self.add(title)
        img_q = ImageMobject("assets/DALLE_Q.png").shift(DOWN * 0.5)

        self.add(img_q)

        self.wait(1)
        # clip
        # difusion
