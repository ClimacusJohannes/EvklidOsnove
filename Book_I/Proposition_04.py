from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np
import math

from modules import Proposition as p
from Proposition_02 import *
from Triangles import ScaleneTriangle


class Proposition_IV(Scene):
    def construct(self):

        title = "Knjiga I, Izrek IV."
        prop = "Če imata dva trikotnika enaki stranici\nin je med njima enak kot,\nimata enaka tudi druga dva kota in stranico."
        
        p.display_text(self, title, prop)

        points=np.array([2 * LEFT + DOWN * 2, 2 * RIGHT + DOWN, 3 * UP + RIGHT])

        triangle1 = ScaleneTriangle(points[0], points[1], points[2]).set_color(WHITE)
        triangle2 = triangle1.copy()
        triangle1.shift(2*LEFT)
        triangle2.shift(2*RIGHT)


        self.play(Create(triangle1))
        self.play(Create(triangle2))
        self.wait()

        Proposition_IV.construction(self, triangle1, triangle2, initial_construction=True)

        self.wait()

    def construction(scene : Scene, triangle1, triangle2, initial_construction : bool = False):

        initial_index = len(scene.mobjects)

        # assumption for the first triangle
        b1 = Line(start=triangle1.get_vertices()[2], end=triangle1.get_vertices()[0]).set_color(BLUE)
        c1 = Line(start=triangle1.get_vertices()[2], end=triangle1.get_vertices()[1]).set_color(RED)
        a1 = Line(start=triangle1.get_vertices()[1], end=triangle1.get_vertices()[0])
        mfill1 = triangle1.create_angle_between_lines(line1=b1, line2=c1, color=YELLOW, other_angle=True)

        # assumptions for the second triangle
        b2 = Line(start=triangle2.get_vertices()[2], end=triangle2.get_vertices()[0]).set_color(BLUE)
        c2 = Line(start=triangle2.get_vertices()[2], end=triangle2.get_vertices()[1]).set_color(RED)
        a2 = Line(start=triangle2.get_vertices()[1], end=triangle2.get_vertices()[0])
        mfill2 = triangle1.create_angle_between_lines(line1=b2, line2=c2, color=YELLOW, other_angle=True)

        angles = VGroup(mfill1, mfill2)
        scene.play(FadeIn(angles))

        b = VGroup(b1, b2)
        scene.play(FadeIn(b))

        c = VGroup(c1, c2)
        scene.play(FadeIn(c))
        scene.wait()

        triangle1.add(a1)
        triangle1.add(b1)
        triangle1.add(c1)
        triangle1.add(mfill1)

        triangle2.add(a2)
        triangle2.add(b2)
        triangle2.add(c2)
        triangle2.add(mfill2)

        difference = triangle1.get_center() - triangle2.get_center()
        scene.play(triangle1.animate.shift(-difference/2))
        scene.play(triangle2.animate.shift(+difference/2))

        # dokaz

        angleB1 = triangle1.create_angle_between_lines(line1=triangle1.c, line2=triangle1.a, color=BLUE, quadrant=(1,-1), rotate=True, about_point=triangle1.point_b.location, rotate_for=PI)
        # angleB1.shift(RIGHT)
        scene.play(FadeIn(angleB1))

        angleC1 = triangle1.create_angle_between_lines(line1=a1, line2=b1, color=RED, rotate=True, rotate_for=PI, about_point=triangle2.get_vertices()[0], other_angle=True)
        scene.play(FadeIn(angleC1))

        a = Line(start=triangle2.get_vertices()[1], end=triangle2.get_vertices()[0]).set_color(YELLOW)
        scene.play(Create(a))
        
        if initial_construction == False :
            for object in scene.mobjects[initial_index:-1]:
                try:
                    # scene.remove(object)
                    pass
                except:
                    pass
            scene.wait()

        