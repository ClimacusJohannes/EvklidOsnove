from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np
import math

from modules import Proposition as p
from Proposition_2 import *


class Proposition_IV(Scene):
    def construct(self):

        title = "Knjiga I, Izrek IV"
        prop = "Če imata dva trikotnika enaki stranici\nin je med njima enak kot,\nimata enaka tudi druga dva kota in stranico."
        
        p.display_text(self, title, prop)

        points=np.array([2 * LEFT + DOWN * 2, 2 * RIGHT + DOWN, 3 * UP + RIGHT])

        triangle1 = Polygram(points).set_color(WHITE)
        triangle2 = triangle1.copy()
        triangle1.shift(2*LEFT)
        triangle2.shift(2*RIGHT)

        self.play(Create(triangle1))
        self.play(Create(triangle2))
        self.wait()

        
        

        # assumption for first triangle

        b1 = Line(start=points[2]+2*LEFT, end=points[0]+2*LEFT).set_color(BLUE)
        c1 = Line(start=points[2]+2*LEFT, end=points[1]+2*LEFT).set_color(RED)
        a1 = Line(start=points[1]+2*LEFT, end=points[0]+2*LEFT)
        b_len = p.get_line_length(b1)
        c_len = p.get_line_length(c1)
        a_len = p.get_line_length(a1)
        
        angleA1 = Angle(line1=b1, line2=c1, radius=b_len/5).set_color(YELLOW)
        angleA1_helper = Angle(line1=b1, line2=c1, radius=0).set_color(YELLOW)
        q11 = angleA1.points #  save all coordinates of points of angle a1
        q12 = angleA1_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts1 = np.concatenate([q11, q12, q11[0].reshape(1, 3)]) 
        mfill1 = VMobject().set_color(YELLOW)
        mfill1.set_points_as_corners(pnts1).set_fill(YELLOW, opacity=1)

        # assumptions for the second triangle
        b2 = Line(start=points[2]+2*RIGHT, end=points[0]+2*RIGHT).set_color(BLUE)
        c2 = Line(start=points[2]+2*RIGHT, end=points[1]+2*RIGHT).set_color(RED)
        a2 = Line(start=points[1]+2*RIGHT, end=points[0]+2*RIGHT).set_color(RED)
        
        angleA2 = Angle(line1=b2, line2=c2, radius=b_len/5).set_color(YELLOW)
        angleA2_helper = Angle(line1=b2, line2=c2, radius=0).set_color(YELLOW)
        q21 = angleA2.points #  save all coordinates of points of angle a1
        q22 = angleA2_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts2 = np.concatenate([q21, q22, q21[0].reshape(1, 3)]) 
        mfill2 = VMobject().set_color(YELLOW)
        mfill2.set_points_as_corners(pnts2).set_fill(YELLOW, opacity=1)



        angles = VGroup(mfill1, angleA1, mfill2, angleA2)
        self.play(FadeIn(angles))
        # self.play(FadeIn(mfill1))
        # self.add(angleA1)
        angleA1.add(mfill1)

        # self.play(FadeIn(mfill2))
        # self.add(angleA2)
        angleA2.add(mfill2)

        b = VGroup(b1, b2)
        self.play(FadeIn(b))

        c = VGroup(c1, c2)
        self.play(FadeIn(c))
        self.wait()

        triangle1.add(a1)
        triangle1.add(b1)
        triangle1.add(c1)
        triangle1.add(angleA1)

        triangle2.add(b2)
        triangle2.add(c2)
        triangle2.add(angleA2)

        self.play(triangle1.animate.shift(2*RIGHT))
        self.play(triangle2.animate.shift(2*LEFT))

        # dokaz

        angleB1 = p.create_angle_between_lines(self, line1=a1, line2=c1, color=BLUE, rotate=True, rotate_for=(3/2)*PI, about_point=points[1])
        # angleB1.shift(RIGHT)
        self.play(FadeIn(angleB1))

        angleC1 = p.create_angle_between_lines(self, line1=a1, line2=b1, color=RED, rotate=True, rotate_for=PI, about_point=points[0])
        self.play(FadeIn(angleC1))

        a = Line(start=points[1], end=points[0]).set_color(YELLOW)
        self.play(Create(a))
        self.wait()
