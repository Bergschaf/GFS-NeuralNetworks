from manim import *

POINTS = [
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 0),
    (1, 0, 0),
]


def surface_function(u, v):
    dist_to_points = [np.sqrt((u - p[0]) ** 2 + (v - p[1]) ** 2) for p in POINTS]
    if min(dist_to_points) == 0:
        return POINTS[dist_to_points.index(0)][2]
    else:
        # weigh the distance to the points
        weights = [pow(1 / d, 2) for d in dist_to_points]
        weights_sum = sum(weights)
        weights = [w / weights_sum for w in weights]
        print(weights)
        return sum([w * p[2] for w, p in zip(weights, POINTS)])


class S0(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        graph = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-4, 4], x_length=8, y_length=8, z_length=8)
        self.add(graph)
        surface = Surface(
            lambda u, v: np.array([
                u,  # x
                v,  # y
                surface_function(u, v)  # z
            ])).scale(4)
        self.add(surface)
