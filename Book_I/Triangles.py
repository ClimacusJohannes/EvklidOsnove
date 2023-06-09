from manim import *
from manim import WHITE
from modules import Proposition as p 
from Book_I_Definitions import Book_I_Definitions
from manim.utils.color import Color


class ScaleneTriangle(Polygram):
    def __init__(self, point_a, point_b, point_c, color=WHITE, **kwargs):
        super().__init__([point_a, point_b, point_c, point_a], color=color, **kwargs)

        self.a = Line(start=point_b, end=point_c)
        self.add(self.a)
        self.a_opposite = Line(start=point_c, end=point_b)
        self.b = Line(start=point_a, end=point_c)
        self.add(self.b)
        self.b_opposite = Line(start=point_c, end=point_a)
        self.c = Line(start=point_a, end=point_b)
        self.add(self.c)
        self.c_opposite = Line(start=point_b, end=point_a)

        self.point_A = Dot(point_a)
        self.point_B = Dot(point_b)
        self.point_C = Dot(point_c)

        self.lines = {
            "a" : self.a,
            "b" : self.b,
            "c" : self.c
        }

        self.dots = {
            "A" : self.point_A,
            "B" : self.point_B,
            "C" : self.point_C,
        }

        self.angles = {}
        self.calculate_angles()

        self.heights = {}
        self.calculate_heights()

    def calculate_angles(self):
        for angle in ["alpha", "beta", "gamma"]:
            value = self.calculate_individual_angle(angle)

            self.angles[angle] = value / DEGREES
        print(self.angles)

    def calculate_individual_angle(self, angle : str):
        angle = angle.lower()
        a = 0
        if angle == "alpha":
            a = Angle(self.b, self.c)
            if a.get_value() > PI :
                a = Angle(self.b, self.c, other_angle=True)
        elif angle == "beta":
            a = Angle(self.c_opposite, self.a)
            if a.get_value() > PI :
                print(str(a.get_value()) + " is too large...")
                a = Angle(self.c_opposite, self.a, other_angle=True)
        elif angle == "gamma":
            a = Angle(self.a_opposite, self.b_opposite)
            if a.get_value() > PI :
                a = Angle(self.a_opposite, self.b_opposite, other_angle=True)
        else:
            ValueError("A triangle has only three angles: alpha, beta, gamma. You tried to calculate: " + angle)
        
        return abs(a.get_value())

    def calculate_heights(self):
        for line in ["a", "b", "c"]:
            height = self.calculate_individual_height(self.get_dot(line), self.get_line(line))
            name_of_height = "V" + line
            self.heights[name_of_height] = height

    def calculate_individual_height(self, dot : Dot, line : Line):
        return p.get_line_length(Line(start=line.get_projection(dot.get_center()), end=dot.get_center()))

    def get_line(self, line : str):
        line = line.lower()
        if (line != "a") and (line != "b") and (line != "c"):
            ValueError("A triangle has only three lines: a, b and c. You tried to get line: " + line)
        return self.lines[line]

    def get_dot(self, dot : str):
        dot = dot.upper()
        if (dot != "A") and (dot != "B") and (dot != "C"):
            ValueError("A triangle has only three dots/vertices: A, B and C. You tried to get dot: " + dot)
        return self.dots[dot]

    def create_angle_between_lines(self, line1 : Line, line2 : Line, color=WHITE, rotate=False, rotate_for=0, about_point=ORIGIN, other_angle=False, adjacent_angle=False, quadrant=(1,1)) -> Mobject:
        line1_len = p.get_line_length(line1)
        line2_len = p.get_line_length(line2)
        
        angle = Angle(line1=line1, line2=line2, radius=min(line1_len, line2_len)/5, quadrant=quadrant, other_angle=other_angle).set_color(color)
        angle_helper = Angle(line1=line1, line2=line2, radius=0, quadrant=quadrant, other_angle=other_angle).set_color(color)
        q1 = angle.points #  save all coordinates of points of angle a1
        q2 = angle_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)]) 
        mfill = VMobject()
        mfill.set_points_as_corners(pnts).set_fill(color, opacity=0.5)

        if rotate:
            mfill.rotate(angle=rotate_for, about_point=about_point)
        final = mfill

        return final.set_color(color)

    def get_angle_figures(self, colors = [WHITE, WHITE, WHITE], rotate=(0, 0, 0), quadrant=((1,1), (1,1), (1,1)), other_angle=(False, False, False)) -> VGroup:

        alpha = self.create_angle_between_lines(self.b, self.c, color=colors[0], rotate = True, rotate_for=rotate[0], about_point=self.get_vertices()[0], quadrant=quadrant[0], other_angle=other_angle[0])
        beta = self.create_angle_between_lines(self.a, self.c, color=colors[1], rotate = True, rotate_for=rotate[1], about_point=self.get_vertices()[1], quadrant=quadrant[1], other_angle=other_angle[1])
        gama = self.create_angle_between_lines(self.a, self.b, color=colors[2], rotate = True, rotate_for=rotate[2], about_point=self.get_vertices()[2], quadrant=quadrant[2], other_angle=other_angle[2])

        return VGroup(alpha, beta, gama)
    
    def get_points(self):
        return self.get_vertices
    
    def set_line_color(self, line : str, color):
        self.lines[line].set_color(color)

    def show_points(self, scene : Scene, color=WHITE):
        points = self.get_vertices()
        print(self.get_vertices())
        print(points)

        dot_a = Dot(points[2], radius=0.05, color=color) 
        dot_b = Dot(points[1], radius=0.05, color=color) 
        dot_c = Dot(points[0], radius=0.05, color=color) 

        tex_a = Tex('A').scale(0.5)
        tex_b = Tex('B').scale(0.5)
        tex_c = Tex('C').scale(0.5)

        tex_a.shift(dot_a.get_center())
        tex_b.shift(dot_b.get_center())
        tex_b.shift(dot_c.get_center())

        self.add(dot_a)
        self.add(dot_b)
        self.add(dot_c)

        group = VGroup(dot_a, dot_b, dot_c)

        scene.play(FadeIn(group))

    def color_angle(self, scene : Scene, angle : str, color : Color = YELLOW):
        if angle == "alpha":
            a = Angle(self.b, self.c)
            if a.get_value() > PI :
                Book_I_Definitions.Definition_IX(scene, self.b, self.c, other_angle=True, color=color) 
            else:          
                Book_I_Definitions.Definition_IX(scene, self.b, self.c, other_angle=False, color=color)           
        elif angle == "beta":
            a = Angle(self.c_opposite, self.a)
            if a.get_value() > PI :
                Book_I_Definitions.Definition_IX(scene, self.c_opposite, self.a, other_angle=True, color=color)
            else:
                Book_I_Definitions.Definition_IX(scene, self.c_opposite, self.a, other_angle=False, color=color)
        elif angle == "gamma":
            a = Angle(self.a_opposite, self.b_opposite)
            if a.get_value() > PI :
                Book_I_Definitions.Definition_IX(scene, self.a_opposite, self.b_opposite, other_angle=True, color=color)
            else:
                Book_I_Definitions.Definition_IX(scene, self.a_opposite, self.b_opposite, other_angle=False, color=color)
        else:
            ValueError("A triangle has only three angles: alpha, beta, gamma. You tried to color: " + angle)


class RightTriangle(ScaleneTriangle):
    def __init__(self, point_a, point_b, point_c, color=WHITE, **kwargs):

        (point_a, point_b, point_c) = self.rearange_points(point_a, point_b, point_c)

        super().__init__(point_a, point_b, point_c, color, **kwargs)

        

    def rearange_points():
        pass