from manim import *
from Triangles import ScaleneTriangle
import Book_I_Definitions as definitions

class JustTrying(Scene):
    def construct(self):

        line1 = Line(start=LEFT, end=RIGHT)
        line2 = Line(start=LEFT, end=UP)
        angle = Angle(line1, line2, color=WHITE)

        self.add(line1, line2, angle)
        print(angle.get_value() / DEGREES)

        triangle = ScaleneTriangle(4*LEFT+2*DOWN, 4*RIGHT+2*DOWN, 2*UP)

        self.add(triangle)
        triangle.color_angle(self, "alpha", color = BLUE)
        triangle.color_angle(self, "beta", color=GREEN)
        triangle.color_angle(self, "gamma", color=RED)