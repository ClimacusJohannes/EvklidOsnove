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

        Proposition_IV.construction(self, points, triangle1, triangle2, initial_construction=True)

        self.wait()

        scene.play(Create(triangle1))
        scene.play(Create(triangle2))
        scene.wait()

    def construction(scene : Scene, triangle1, triangle2, initial_construction : bool = False):

        initial_index = len(scene.mobjects)

        b1 = Line(start=triangle1.get_vertices()[2], end=triangle1.get_vertices()[0]).set_color(BLUE)
        c1 = Line(start=triangle1.get_vertices()[2], end=triangle1.get_vertices()[1]).set_color(RED)
        a1 = Line(start=triangle1.get_vertices()[1], end=triangle1.get_vertices()[0])
        b_len = p.get_line_length(b1)
        c_len = p.get_line_length(c1)
        a_len = p.get_line_length(a1)
        
        angleA1 = Angle(line1=b1, line2=c1, radius=b_len/5, other_angle=True).set_color(YELLOW)
        angleA1_helper = Angle(line1=b1, line2=c1, radius=0, other_angle=True).set_color(YELLOW)
        q11 = angleA1.points #  save all coordinates of points of angle a1
        q12 = angleA1_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts1 = np.concatenate([q11, q12, q11[0].reshape(1, 3)]) 
        mfill1 = VMobject().set_color(YELLOW)
        mfill1.set_points_as_corners(pnts1).set_fill(YELLOW, opacity=1)

        # assumptions for the second triangle
        b2 = Line(start=triangle2.get_vertices()[2], end=triangle2.get_vertices()[0]).set_color(BLUE)
        c2 = Line(start=triangle2.get_vertices()[2], end=triangle2.get_vertices()[1]).set_color(RED)
        a2 = Line(start=triangle2.get_vertices()[1], end=triangle2.get_vertices()[0]).set_color(RED)
        
        angleA2 = Angle(line1=b2, line2=c2, radius=b_len/5, other_angle=True).set_color(YELLOW)
        angleA2_helper = Angle(line1=b2, line2=c2, radius=0, other_angle=True).set_color(YELLOW)
        q21 = angleA2.points #  save all coordinates of points of angle a1
        q22 = angleA2_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts2 = np.concatenate([q21, q22, q21[0].reshape(1, 3)]) 
        mfill2 = VMobject().set_color(YELLOW)
        mfill2.set_points_as_corners(pnts2).set_fill(YELLOW, opacity=1)



        angles = VGroup(mfill1, angleA1, mfill2, angleA2)
        scene.play(FadeIn(angles))
        # self.play(FadeIn(mfill1))
        # self.add(angleA1)
        angleA1.add(mfill1)

        # self.play(FadeIn(mfill2))
        # self.add(angleA2)
        angleA2.add(mfill2)

        b = VGroup(b1, b2)
        scene.play(FadeIn(b))

        c = VGroup(c1, c2)
        scene.play(FadeIn(c))
        scene.wait()

        triangle1.add(a1)
        triangle1.add(b1)
        triangle1.add(c1)
        triangle1.add(angleA1)

        triangle2.add(a2)
        triangle2.add(b2)
        triangle2.add(c2)
        triangle2.add(angleA2)

        difference = triangle1.get_center() - triangle2.get_center()
        scene.play(triangle1.animate.shift(-difference/2))
        scene.play(triangle2.animate.shift(+difference/2))

        # dokaz

        angleB1 = p.create_angle_between_lines(scene, line1=a1, line2=c1, color=BLUE, rotate=True, rotate_for=(3/2)*PI, about_point=triangle2.get_vertices()[1])
        # angleB1.shift(RIGHT)
        scene.play(FadeIn(angleB1))

        angleC1 = p.create_angle_between_lines(scene, line1=a1, line2=b1, color=RED, rotate=True, rotate_for=PI, about_point=triangle2.get_vertices()[0])
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

        