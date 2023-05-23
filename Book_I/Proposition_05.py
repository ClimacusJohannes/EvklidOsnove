from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np
import math
from manim.utils.color import Color

from modules import Proposition as p
from Triangles import ScaleneTriangle
from Proposition_03 import Proposition_III
from Proposition_04 import Proposition_IV

class Proposition_V(Scene):
    
    def construct(self):

        title = "Knjiga I, Izrek V."
        prop = "Za vsak enakokraki trikotnik velja,\n da ima dva enaka kota.\nČe kraka podaljšamo za isto dolžino\nbosta nastala dva kota prav tako enaka."
        
        p.display_text(self, title, prop)

        points = [3/2 * LEFT, 3/2 * RIGHT, (7/2)*UP]

        triangle = ScaleneTriangle(point_a=points[0], point_b=points[1], point_c=points[2])

        self.play(Create(triangle))
        self.play(triangle.animate.set_line_color("a", color=RED))
        self.play(triangle.animate.set_line_color("b", color=RED))
        self.wait()

        # triangle.show_points(self)

        angles = triangle.get_angle_figures(colors=[BLUE, BLUE, ORANGE], rotate=(0, 0, PI), quadrant=((1,1), (1,-1), (1,1)), other_angle=(True, False, True))
        self.play(FadeIn(angles))

        extended_line1 = Line(start=triangle.point_a, end=points[0] - (p.get_line_slope(triangle.b) * 3), color=YELLOW)
        self.play(Create(extended_line1))

        overextended_line = DashedLine(start=triangle.point_b, end=points[1] - (p.get_line_slope(triangle.a) * 10), color=WHITE)
        self.play(Create(overextended_line))

        dot = Dot(points[1], radius=0.01)

        Proposition_III.construction(self, extended_line1, overextended_line, dot)

        extended_line2 = self.mobjects[-2]
        print(self.mobjects)
        print(extended_line2)

        self.play(Uncreate(overextended_line))

        connecting_line1 = Line(start=extended_line1.end, end=triangle.point_b, color=BLUE)
        connecting_line2 = Line(start=extended_line2.end, end=triangle.point_a, color=BLUE)
        connecting_lines = VGroup(connecting_line1, connecting_line2)
        self.play(Create(connecting_lines))
        self.wait()
        print(triangle.get_vertices())
        print(extended_line1.end)

        new_triangle1 = ScaleneTriangle(point_a=triangle.get_vertices()[1], point_b=extended_line1.end, point_c=triangle.get_vertices()[2])
        new_triangle2 = ScaleneTriangle(point_a=triangle.get_vertices()[0], point_b=extended_line2.end, point_c=triangle.get_vertices()[2])


        self.play(Create(new_triangle1))
        self.play(Create(new_triangle2))

        for ob in self.mobjects[:-1]:
            self.remove(ob)

        self.play(new_triangle1.animate.shift(LEFT))
        self.play(new_triangle2.animate.shift(RIGHT))
        self.play(new_triangle2.animate.flip())

        points = new_triangle2.get_vertices()
        new_triangle = ScaleneTriangle(point_a=[points[0][0], points[0][1], 0], point_b=[points[1][0], points[1][1], 0], point_c=[points[2][0], points[2][1], 0])
        self.add(new_triangle)
        self.remove(new_triangle2)
        
        Proposition_IV.construction(self, new_triangle1, new_triangle)

        self.wait()



