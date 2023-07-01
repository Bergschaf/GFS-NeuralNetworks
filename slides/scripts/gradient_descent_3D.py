from manim import *

POINTS = [
    (0, 0, 0.1),
    (0, 0.2, 0.1),
    (0, 1, 0.15),
    # (0, 1, 0),
    (0.2, 0.2, 0.2),
    (0.7, 0.8, 0.4),
    (0.8, 0.65, 0.4),
    (1, 0, 0.4),
    (0.2, 1, 0.2),
    (0.6, 0.35, 0.2),
    (0.4, 0.55, -0.05), # -0.1),
    (0.7, 0.3, 0.15)
]


def surface_function(u, v):
    dist_to_points = [np.sqrt((u - p[0]) ** 2 + (v - p[1]) ** 2) for p in POINTS]
    if min(dist_to_points) == 0:
        return POINTS[dist_to_points.index(0)][2]
    else:
        # weigh the distance to the points
        weights = [pow(1 / d, 3) for d in dist_to_points]
        weights_sum = sum(weights)
        weights = [w / weights_sum for w in weights]
        return sum([w * p[2] for w, p in zip(weights, POINTS)])


def get_surface_cords(u, v):
    return np.array([(u - 0.5) * 4, (v - 0.5) * 4, surface_function(u, v) * 4 - 0.55])


class S0(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.5)
        self.set_camera_orientation(phi=60 * DEGREES, theta=180 * DEGREES, zoom=2.5)

        graph = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-4, 4], x_length=8, y_length=8, z_length=8)
        # +self.add(graph)
        surface = Surface(
            lambda u, v: np.array([
                u,  # x
                v,  # y
                surface_function(u, v)  # z
            ]), resolution=(50, 50)).scale(4)
        surface.set_fill_by_value(axis=2, colors=[(BLUE, -0.4), (GREEN, -0.10), (RED, 1)], axes=graph)
        self.add(surface)
        # position the surface at the origin
        surface.move_to(ORIGIN)

        self.wait(1)

        x_axis = Arrow3D(LEFT * 2, RIGHT * 2).shift(UP * 2.2)
        x_axis_label = MathTex("Paramter\\:x_0").scale(0.8).next_to(x_axis, UP * 0.2)
        self.add(x_axis)
        self.add(x_axis_label)

        y_axis = Arrow3D(UP * 2, DOWN * 2).shift(LEFT * 2.2)
        y_axis_label = MathTex("Paramter\\:x_1").scale(0.8).rotate(-PI / 2).next_to(y_axis, LEFT * 0.5)
        self.add(y_axis)
        self.add(y_axis_label)

        # self.remove(surface)
        self.wait(1)

        global_minimum = Dot3D(get_surface_cords(0.4, 0.55), color=RED, radius=0.05)
        global_minimum_label = Text("Globales Minimum", color=RED).scale(1).next_to(global_minimum, DOWN * 5)

        self.add(global_minimum)
        self.add_fixed_in_frame_mobjects(global_minimum_label)

        self.wait(1)

        local_minimum = Dot3D(get_surface_cords(0.7, 0.3), color=BLUE, radius=0.05)
        local_minimum_label = Text("Lokales Minimum", color=BLUE).scale(1)
        


        self.add(local_minimum)
        self.add_fixed_in_frame_mobjects(local_minimum_label.shift(RIGHT * 2.5 + UP * 1.7))

        self.wait(1)

        point = Dot3D(get_surface_cords(0.67, 0.75), color=YELLOW, radius=0.05)
        point_label = Text("Zufälliger Startpunkt", color=YELLOW).scale(1).shift(UP * 2.4 + LEFT * 2.5)

        self.add(point)
        self.add_fixed_in_frame_mobjects(point_label)

        self.wait(1)

        self.remove(local_minimum_label, global_minimum_label, point_label)




