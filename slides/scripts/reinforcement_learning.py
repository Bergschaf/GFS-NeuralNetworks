from manim import *


class S0(Scene):
    def construct(self):
        title = Title("Reinforcement Learning")
        self.add(title)

        reinforcement = ["Reinforcement Learning", "Lernen durch Interaktion mit der Umgebung",
                         "Belohnungen oder Bestrafungen"]
        supervised = ["Supervised Learning", "Lernen mit einem gelabelten Datenset", "Kostenfunktion"]
        reinforcement_list = BulletedList(*reinforcement).scale(0.9).shift(UP * 1)
        supervised_list = BulletedList(*supervised).scale(0.9).shift(DOWN * 1.5).align_to(reinforcement_list, LEFT)
        reinforcement_list[0].set_color(YELLOW)
        supervised_list[0].set_color(YELLOW)

        self.add(reinforcement_list, supervised_list)

        self.wait(1)

        self.clear()
        title = Title("Reinforcement Learning - Genetische Algorithmen")
        self.add(title)

        self.wait(1)

        bulleted_list = ["Population: Eine Menge von verschiedenen Individuen wird erstellt",
                         "Auswahl: Die Individuen werden nach ihrer Fitness ausgewählt",
                         "Rekombination: Die besten Individuen werden kombiniert",
                         "Mutation: Die neuen Individuen werden zufällig verändert"]

        list = BulletedList(*bulleted_list).scale(0.9)
        self.add(list)

        self.wait(1)




