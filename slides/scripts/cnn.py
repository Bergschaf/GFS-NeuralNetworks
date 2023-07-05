from manim import *

import numpy as np

from colour import Color

import random


class ThreeDSceneSquareGrid(ThreeDScene):

    def create_grid(self, xx, yy, fill_colors, cell_numbers=None, fill_opacities=0.8,
                    stroke_colors=(1.0, 1.0, 1.0),
                    side_length=1):

        class Grid:

            def __init__(self, xx, yy, fill_colors, fill_opacities, stroke_colors, side_length):

                class SquareCell:

                    def __init__(self, square, x, y, number):
                        self.square = square
                        self.x = x
                        self.y = y
                        self.number = number

                self.xx = xx
                self.yy = yy
                self.fill_colors = fill_colors
                self.fill_opacities = fill_opacities
                self.stroke_colors = stroke_colors
                self.side_length = side_length

                self.grid = []

                for i, y in enumerate(reversed(yy)):
                    for j, x in enumerate(xx):
                        square = Square(side_length=side_length)
                        if cell_numbers is not None:
                            cell = SquareCell(square, x, y, DecimalNumber(number=cell_numbers[j][i]).scale(0.8))
                            cell.number.set_x(x * side_length).set_y(y * side_length)
                        else:
                            cell = SquareCell(square, x, y, None)

                        cell.square.set_x(x * side_length)
                        cell.square.set_y(y * side_length)

                        self.grid.append(cell)

                self = self.update_colors(fill_colors=self.fill_colors, stroke_colors=self.stroke_colors)
                self = self.update_opacities(fill_opacities=self.fill_opacities)

            def colors2rgb(self, colors, x, y):
                # RGB image (scaled to [0,1])
                if type(colors) == np.ndarray and colors.ndim == 3:
                    color_rgb = tuple(colors[x, y, :])
                # Grayscalage image (scaled to [0.1])
                elif type(colors) == np.ndarray and colors.ndim == 2:
                    color_rgb = (colors[x, y], colors[x, y], colors[x, y])
                # solid color, RGB Tuple
                elif type(colors) == tuple and len(colors) == 3:
                    color_rgb = colors
                else:
                    raise ValueError("Check color type")

                return color_rgb

            def update_colors(self, fill_colors=None, stroke_colors=None):
                cell_count = 0
                for x in range(len(xx)):
                    for y in range(len(yy)):
                        fill_color = Color(rgb=self.colors2rgb(fill_colors, x, y)) if fill_colors is not None else None

                        stroke_color = Color(
                            rgb=self.colors2rgb(stroke_colors, x, y)) if stroke_colors is not None else None

                        self.grid[cell_count].square.set_fill(color=fill_color)
                        self.grid[cell_count].square.set_stroke(color=stroke_color)
                        cell_count += 1

                self.fill_colors = fill_colors
                self.stroke_colors = stroke_colors

                return self

            def update_opacities(self, fill_opacities):
                cell_count = 0
                for x in xx:
                    for y in yy:

                        if type(fill_opacities) == int or type(fill_opacities) == float:
                            fill_opacity = (fill_opacities, fill_opacities, fill_opacities)
                        elif type(fill_opacities) == np.ndarray:
                            fill_opacity = fill_opacities[x, y]

                        else:
                            raise ValueError("check opacities value")

                        self.grid[cell_count].square.set_opacity(fill_opacity)
                        cell_count += 1

                self.fill_opacities = fill_opacities

                return self

            def shift_grid(self, x_increment=None, y_increment=None, z_increment=None, step_size=self.side_length):
                for cell in self.grid:
                    if x_increment:
                        current_x = cell.square.get_x()
                        if cell_numbers is not None:
                            cell.number.set_x(current_x + x_increment * step_size)
                        cell.square.set_x(current_x + x_increment * step_size)
                    if y_increment:
                        current_y = cell.square.get_y()
                        if cell_numbers is not None:
                            cell.number.set_y(current_y + y_increment * step_size)
                        cell.square.set_y(current_y + y_increment * step_size)
                    if z_increment:
                        current_z = cell.square.get_z()
                        cell.square.set_z(current_z + z_increment * step_size)
                        if cell_numbers is not None:
                            cell.number.set_z(current_z + z_increment * step_size)

        return Grid(xx, yy, fill_colors, fill_opacities=fill_opacities, stroke_colors=stroke_colors,
                    side_length=self.side_length)


class S0(ThreeDSceneSquareGrid):

    def construct(self):
        title = Title("Convoluational Neural Networks")
        self.add(title)
        self.side_length = 0.9

        self.set_camera_orientation(phi=3 * PI / 8, gamma=0, zoom=0.9)
        xx = np.arange(-6, 0)
        yy = np.arange(-3, 3)
        grid_numbers = [[random.random() for _ in range(6)] for _ in range(6)]
        simple_grid = self.create_grid(xx, yy, (0, 0, 0.9), cell_numbers=grid_numbers, side_length=self.side_length)
        simple_grid.shift_grid(x_increment=-1)

        faltungsmatrix = [[0.5, -0.1, 0.5], [-0.2, 0.7, -0.2], [0.5, -0.1, 0.5]]

        result = calculate_result(grid_numbers, faltungsmatrix)
        conv_result = self.create_grid(np.arange(3, 7), np.arange(-2, 2), fill_colors=(0, 0.8, 0),
                                       side_length=self.side_length, cell_numbers=result)
        conv_result.shift_grid(x_increment=1)

        for cell in simple_grid.grid:
            self.add(cell.square, cell.number)

        xx = np.arange(-7, -4)
        yy = np.arange(0, 3)

        kernel = self.create_grid(xx, yy, fill_colors=(1, 1, 0), side_length=self.side_length)

        xx = np.arange(0, 3)
        yy = np.arange(0, 3)

        faltungsmatrix_grid = self.create_grid(xx, yy, fill_colors=(1, 1, 0), side_length=self.side_length,
                                               cell_numbers=faltungsmatrix)
        faltungsmatrix_grid.shift_grid(y_increment=-1.5)

        yy = np.arange(-4, 0)
        xx = np.arange(0, 4)

        result_outline_grid = self.create_grid(xx, yy, fill_colors=(0, 0, 0), side_length=self.side_length, )
        result_outline_grid.shift_grid(y_increment=2, x_increment=4)
        for cell in result_outline_grid.grid:
            self.add(cell.square)

        for cell in kernel.grid:
            self.add(cell.square)

        for cell in faltungsmatrix_grid.grid:
            self.add(cell.square, cell.number)

        self.set_camera_orientation(phi=0, gamma=0, distance=50)
        count = 0
        for ii in range(4):
            for jj in range(4):

                if count < len(conv_result.grid):

                    self.add(conv_result.grid[count].square, conv_result.grid[count].number)
                    count += 1
                    if ii < 1:
                        self.wait(1)
                    if jj != 3:
                        kernel.shift_grid(x_increment=1)

            if count < len(conv_result.grid):
                kernel.shift_grid(x_increment=-3, y_increment=-1)
                self.wait(1)

        self.wait(1)
        self.clear()
        self.add(title)
        # ------------------------------------------

        self.side_length = 0.8

        self.move_camera(phi=3 * PI / 8, gamma=0)
        xx = np.arange(-6, 2)
        yy = np.arange(-4, 4)

        grid_numbers = [[random.random() for _ in range(8)] for _ in range(8)]

        simple_grid = self.create_grid(xx, yy, fill_colors=(0, 1, 0), side_length=self.side_length,
                                       cell_numbers=grid_numbers)
        simple_grid.shift_grid(y_increment=-0.5)
        pool_result = get_Pool_result(grid_numbers)
        pool_result = self.create_grid(np.arange(4, 8), np.arange(-2, 2), fill_colors=(0, 111 / 255, 1),
                                       side_length=self.side_length, cell_numbers=pool_result)
        pool_result.shift_grid(y_increment=-0.5, x_increment=-0.5)
        for cell in simple_grid.grid:
            self.add(cell.square, cell.number)

        xx = np.arange(-6, -4)
        yy = np.arange(2, 4)

        kernel_cols = np.ones((2, 2, 3))
        kernel_cols[:, :, 2] = 0
        kernel = self.create_grid(xx, yy, fill_colors=kernel_cols, side_length=self.side_length)
        kernel.shift_grid(y_increment=-0.5)
        self.set_camera_orientation(phi=0, gamma=0)
        self.wait(1)

        for cell in kernel.grid:
            self.add(cell.square)

        self.wait(1)
        #  self.add(conv_result.grid[0].square)

        count = 0
        for ii in range(4):
            for jj in range(4):

                if count < len(pool_result.grid):

                    self.add(pool_result.grid[count].square, pool_result.grid[count].number)
                    count += 1
                    if ii < 1:
                        self.wait(1)
                    kernel.update_colors(kernel_cols)
                    if jj != 3:
                        kernel.shift_grid(x_increment=2)

            if count < len(pool_result.grid):
                kernel.shift_grid(x_increment=-6, y_increment=-2)
                self.wait(1)

            else:
                print("here")
                break
                #  count+=1
        self.wait(1)

        self.clear()
        self.add(title)
        self.wait(1)
        bullet_points = [
            "Kombination aus Convolution und Pooling",
            "Convolution: Erkennen von Mustern",
            "Pooling: Reduzierung der Datenmenge",
            "Wird oft für Bilderkennung verwendet",
            "Deutlich effizienter als vollständig verbundene Netze"]
        bullet_list = BulletedList(*bullet_points).shift(DOWN * 0.5)

        for i in range(len(bullet_points)):
            self.add(bullet_list[i])
            self.wait(1)


def calculate_result(grid, faltung):
    result = []
    rand = len(faltung) // 2
    for i, y in enumerate(grid[rand:-rand]):
        result.append([])
        for j, x in enumerate(y[rand:-rand]):
            res = 0
            for k in range(len(faltung)):
                for l in range(len(faltung)):
                    res += faltung[k][l] * grid[i - rand + k][j - rand + l]
            result[i].append(res)

    print(result)
    return result


def get_Pool_result(grid):
    res = []
    c = 0
    for i in range(0, len(grid) - 1, 2):

        res.append([])
        for j in range(0, len(grid[i]) - 1, 2):
            res[c].append(max([grid[i][j], grid[1 + i][j], grid[i][1 + j], grid[1 + i][1 + j]]))

        c += 1
    return res
