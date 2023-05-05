from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np
from modules import Proposition as p
from Proposition_2 import *

# config.background_color = '#fcf3d9'
class Proposition_III(Scene):
    def construct(self):
        title=Text('Knjiga I, izjava III\n Problem.').scale(2)
        prop=Text('Od večje od dveh danih črt izriši del enak manjši.')
        p.display_text(self, title, prop)

        line1 = Line(start=(DOWN + RIGHT), end=(RIGHT)) # krajsa daljica
        line2 = Line(start=(LEFT + UP), end= 1 * RIGHT + UP) # daljsa daljiva
        dot = Dot(line2.start)

        self.add(line1)
        self.add(line2)
        self.play(Create(dot))

        Proposition_II.construction(self, line1, dot)

        line_eq_line1 = self.mobjects[-2]

        print(self.mobjects)
        circle = Circle(radius=p.get_line_length(line_eq_line1)).set_color(BLUE).shift(dot.get_arc_center())
        self.play(Create(circle))

        dot2 = Dot(line2.start + (p.get_line_length(line_eq_line1) * p.get_line_slope(line2))).set_color(YELLOW)
        self.play(Create(dot2))
        dot3 = Dot(line2.start).set_color(YELLOW)
        self.play(Create(dot3))


        # part_of_line = line_eq_line1.copy().set_color(YELLOW)
        part_of_line = Line(start=dot.get_arc_center(), end=dot2.get_arc_center()).set_color(YELLOW)
        self.play(Create(part_of_line))
        # self.play(Rotate(part_of_line, - (PI - (line2.get_angle() - line_eq_line1.get_angle())), about_point=dot.get_arc_center()))
        self.wait()

    def construction():
        pass