from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np
from modules import Proposition as p
from Proposition_02 import *

# config.background_color = '#fcf3d9'
class Proposition_III(Scene):
    def construct(self):
        title=Text('Knjiga I, izjava III.').scale(2)
        prop=Text('Od večje od dveh danih črt izriši del enak manjši.')
        p.display_text(self, title, prop)

        line1 = Line(start=(DOWN + RIGHT), end=(RIGHT)) # krajsa daljica
        line2 = Line(start=(LEFT + UP), end= 1 * RIGHT + UP) # daljsa daljica
        dot = Dot(line2.start)

        Proposition_III.construction(self, line1, line2, dot, initial_construction=True)

    def construction(scene, line1, line2, dot, initial_construction : bool = False):

        initial_index = len(scene.mobjects)

        scene.add(line1)
        scene.add(line2)
        scene.play(Create(dot))

        Proposition_II.construction(scene, line1, dot)

        line_eq_line1 = scene.mobjects[-2]

        print(scene.mobjects)
        circle = Circle(radius=p.get_line_length(line_eq_line1)).set_color(BLUE).shift(dot.get_arc_center())
        scene.play(Create(circle))

        dot2 = Dot(line2.start + (p.get_line_length(line_eq_line1) * p.get_line_slope(line2))).set_color(YELLOW)
        # scene.play(Create(dot2))
        dot3 = Dot(line2.start).set_color(YELLOW)
        # scene.play(Create(dot3))


        # part_of_line = line_eq_line1.copy().set_color(YELLOW)
        part_of_line = Line(start=dot.get_arc_center(), end=dot2.get_arc_center()).set_color(YELLOW)
        scene.play(Rotate(line_eq_line1, - (PI - (line2.get_angle() - line_eq_line1.get_angle())), about_point=dot.get_arc_center()))
        scene.play(Create(part_of_line))
        
        # scene.wait()

        if initial_construction == False :
            for object in scene.mobjects[initial_index:-1]:
                try:
                    scene.remove(object)
                except:
                    pass
            scene.wait()