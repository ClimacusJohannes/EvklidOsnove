from manim import *
from modules import Proposition as p

# triangle1 = Polygram(points).set_color(WHITE).round_corners()

# class ColoredAngle(Mobject):
    
#     def __init__(self, line1, line2):
#         line1_len = p.get_line_length(line1)
#         line2_len = p.get_line_length(line2)
        
#         angle = Angle(line1=line1, line2=line2, radius=min(line1_len, line2_len)/5).set_color(color)
#         angle_helper = Angle(line1=line1, line2=line2, radius=0).set_color(color)
#         q1 = angle.points #  save all coordinates of points of angle a1
#         q2 = angle_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
#         pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)]) 
#         super().set_points_as_corners(pnts).set_fill(color, opacity=1)


    

class ScaleneTriangle(Polygram):
    def __init__(self, point_a, point_b, point_c, color=WHITE, **kwargs):
        super().__init__([point_a, point_b, point_c, point_a], color=color, **kwargs)

        # self.points = self.get_vertices()

        self.a = Line(start=point_b, end=point_c)
        self.add(self.a)
        self.b = Line(start=point_a, end=point_c)
        self.add(self.b)
        self.c = Line(start=point_a, end=point_b)
        self.add(self.c)

        self.point_a = Point(point_a)
        self.point_b = Point(point_b)
        self.point_c = Point(point_c)

        self.lines = {
            "a" : self.a,
            "b" : self.b,
            "c" : self.c
        }

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
            
        if adjacent_angle:
            # final = self.get_adjacent_angle(mfill, line1)
            pass
        # else:
        final = mfill

        print("Returning:")
        print(final)
        print("Instead of")
        print(mfill)

        return final.set_color(color)
    
    def get_adjacent_angle(self, mfill : VMobject, line1 : Line):
        
        line2 = Line(start=line1.start, end=line1.end)

        full_angle_figure = self.create_angle_between_lines(line1, line2)
        print("I got to here!")

        return Difference(mfill, full_angle_figure, color=GREEN, fill_opacity=1)
        

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

