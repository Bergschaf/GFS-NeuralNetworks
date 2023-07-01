from manim import *


class S0(Scene):
    def construct(self):
        title = Title("Backpropagation")
        self.add(title)

        cost_derivative = MathTex(
            r"\frac{\partial C}{\partial w_{ij}^{L}} = \frac{\partial C}{\partial o_{i}^L} \frac{\partial o_{i}^L}{\partial net_{i}^L} \frac{\partial net_{i}^L}{\partial w_{ij}^L}") \
            .scale(1.2)
        cost_derivative[0][0:2].set_color(RED)
        cost_derivative[0][3:8].set_color(YELLOW)
        cost_derivative[0][9:11].set_color(RED)
        cost_derivative[0][12:16].set_color(BLUE)
        cost_derivative[0][16:20].set_color(BLUE)
        cost_derivative[0][21:27].set_color(GREEN)
        cost_derivative[0][27:33].set_color(GREEN)
        cost_derivative[0][34:39].set_color(YELLOW)

        self.add(cost_derivative)

        self.wait(1)

        cost_derivative.scale(0.8).shift(UP * 1.8 + LEFT * 3)

        cost_derivative_output = MathTex(r"\frac{\partial C}{\partial o_{i}^{L_{-1}}} = t_i - o_{i}^{L_{-1}}").scale(
            1.2)
        cost_derivative_output[0][0:2].set_color(RED)
        cost_derivative_output[0][3:9].set_color(BLUE)
        cost_derivative_output[0][10:12].set_color(GREEN)
        cost_derivative_output[0][13:18].set_color(BLUE)

        self.add(cost_derivative_output)

        cost_calc = MathTex(r"C = \frac{1}{2} \sum_{i=1}^{n} (o_{i}^{L_{-1}} - t_i)^2").scale(1.2).shift(
            RIGHT * 2.5 + UP * 1)

        cost_calc[0][0].set_color(RED)
        cost_calc[0][11:16].set_color(BLUE)
        cost_calc[0][17:19].set_color(GREEN)

        self.add(cost_calc.next_to(cost_derivative_output, DOWN * 1.5))

        gilt_nur_für_letzten_layer = Tex("$\\rightarrow$ gilt nur für den letzten Layer").scale(0.8).next_to(cost_calc,
                                                                                                             DOWN * 1)

        self.add(gilt_nur_für_letzten_layer)

        self.wait(1)

        self.remove(cost_calc)
        cost_derivative_output.scale(0.8).next_to(cost_derivative, DOWN * 2).shift(LEFT * 0.8)
        gilt_nur_für_letzten_layer.scale(0.8).next_to(cost_derivative_output, DOWN * 0.5)

        output_derivative_net = MathTex(r"\frac{\partial o_{i}^L}{\partial net_{i}^L} = \sigma’ (net_{i}^L)").scale(
            1.2)

        output_derivative_net[0][0:4].set_color(BLUE)
        output_derivative_net[0][5:11].set_color(GREEN)
        output_derivative_net[0][15:20].set_color(GREEN)

        self.add(output_derivative_net.shift(DOWN * 2))

        self.wait(1)

        output_derivative_net.scale(0.8).next_to(gilt_nur_für_letzten_layer, DOWN * 2).shift(LEFT * 0.1)

        self.wait(1)

        net_derivative_weight = MathTex(r"\frac{\partial net_{i}^L}{\partial w_{ij}^L} = o_{j}^{L-1}").scale(1.2)

        net_derivative_weight[0][0:6].set_color(GREEN)
        net_derivative_weight[0][7:12].set_color(YELLOW)
        net_derivative_weight[0][13:19].set_color(BLUE)

        self.add(net_derivative_weight.shift(RIGHT * 2 + DOWN * 1))

        self.wait(1)

        self.clear()
        self.add(title)
        self.add(cost_derivative.center().shift(UP * 1.8).scale(1.2))

        cost_derivative_last_layer = MathTex(
            r"\frac{\partial C}{\partial w_{ij}^{L}} = (t_i - o_{i}^L) \cdot \sigma’ (net_{i}^L) \cdot o_{j}^{L-1}").scale(
            1.2)
        cost_derivative_last_layer[0][0:2].set_color(RED)
        cost_derivative_last_layer[0][3:8].set_color(YELLOW)
        cost_derivative_last_layer[0][10:12].set_color(GREEN)
        cost_derivative_last_layer[0][13:16].set_color(BLUE)
        cost_derivative_last_layer[0][21:26].set_color(GREEN)
        cost_derivative_last_layer[0][28:33].set_color(BLUE)

        self.add(cost_derivative_last_layer.next_to(cost_derivative, DOWN * 1.5),
                 gilt_nur_für_letzten_layer.next_to(cost_derivative_last_layer, DOWN * 0.1).scale(1.2))

        self.wait(1)
        cost_derivative_last_layer.scale(0.8).next_to(cost_derivative, DOWN * 1)
        gilt_nur_für_letzten_layer.scale(1).next_to(cost_derivative_last_layer, DOWN * 0.1)
        cost_derivative_hidden_layer = MathTex(
            r"\frac{\partial C}{\partial w_{ij}^{L}} = \sigma’ (net_{i}^L) \cdot o_{j}^{L-1} \cdot \sum^{n}_{k=1}{\frac{\partial C}{\partial net^{L+1}_k}").scale(
            1.2)
        cost_derivative_hidden_layer[0][0:2].set_color(RED)
        cost_derivative_hidden_layer[0][3:8].set_color(YELLOW)
        cost_derivative_hidden_layer[0][12:17].set_color(GREEN)
        cost_derivative_hidden_layer[0][19:24].set_color(BLUE)
        cost_derivative_hidden_layer[0][30:32].set_color(RED)
        cost_derivative_hidden_layer[0][33:41].set_color(GREEN)

        self.add(cost_derivative_hidden_layer.next_to(cost_derivative_last_layer, DOWN * 2.5))

        gilt_auch_für_hidden_layer = Tex("$\\rightarrow$ gilt auch für hidden Layer").scale(0.8).next_to(
            cost_derivative_hidden_layer, DOWN * 1)
        self.add(gilt_auch_für_hidden_layer)

        self.wait(1)

        self.clear()
        self.add(title)

        delta_weight = MathTex(r"\Delta w_{ij}^L = - \eta \cdot \frac{\partial C}{\partial w_{ij}^L}").scale(1.2)

        delta_weight[0][0:5].set_color(RED_A)
        delta_weight[0][9:11].set_color(RED)
        delta_weight[0][12:17].set_color(YELLOW)

        self.add(delta_weight)

        self.wait(1)

        delta_weight.scale(0.9).shift(UP * 1)

        weight_new = MathTex(r"w_{ij}^{L\:neu} = w_{ij}^{L\:alt} + \Delta w_{ij}^L").scale(1.2).shift(DOWN * 1)

        weight_new[0][0:7].set_color(YELLOW)
        weight_new[0][8:15].set_color(YELLOW)
        weight_new[0][16:21].set_color(RED_A)

        self.add(weight_new)
        self.wait(1)
