from manim import *
import numpy as np

class Proposition():
    def display_text(scene : Scene, title: str, prop: str): 
        if (type(title) != Text) and type(title) == str:
            title = Text(title)
        else:
            TypeError('The title is supposed to be either a Text or a str.')
        if (type(prop) != Text) and type(prop) == str:
            prop = Text(prop)
        else:
            TypeError('The prop is supposed to be either a Text or a str.')
        scene.play(Create(title))
        scene.wait()
        scene.remove(title)
        scene.play(Create(prop))
        scene.wait()
        scene.wait()
        scene.wait()
        scene.remove(prop)
        scene.wait()

    def rotate(circle : Circle):
        previous = circle.get_anchors_and_handles()
        center = circle.get_arc_center()
        new : np.ndarray = []
        for point in previous:
            new.append(point * np.array([ -1, 1 , 0 ]))
        # print(new)
        circle.set_anchors_and_handles(new[0], new[1], new[2], new[3])
        circle.shift(2 * center * RIGHT)

    def get_line_length(line : Line):
        return np.linalg.norm(line.end - line.start)
    
    def get_line_slope(line : Line):
        return (line.end - line.start) / np.linalg.norm(line.end - line.start)
         
    def create_extended_line(line : Line, for_len : float, from_end : bool = True):
        slope = Proposition.get_line_slope(line)
        if from_end:
            end = line.end + slope * for_len
            return Line(start=line.start, end=end)
        else:
            start = line.start - slope * for_len
            return Line(start=start, end=line.end)
    
    def add_two_lines() -> Line:
        pass

    def subtract_two_lines(line1 : Line, line2 : Line):
        if line1.get_slope() != line2.get_slope():
            raise ValueError('Lines should be parallel.')
        if all(line1.start) == all(line2.start):
            diff = line1.end - line2.end
            end = line1.end - diff
            return Line(start=line1.start, end=end)
        if all(line1.end) == all(line2.end):
            diff = line1.start - line2.start
            start = line1.start - diff
            return Line(start=start, end=line1.end)
        else:
            raise ValueError('Lines must have one point in common.')
        
    def create_angle_between_lines(scene: Scene, line1 : Line, line2 : Line, color=WHITE, rotate=False, rotate_for=0, about_point=ORIGIN) -> Mobject:
        line1_len = Proposition.get_line_length(line1)
        line2_len = Proposition.get_line_length(line2)
        
        angle = Angle(line1=line1, line2=line2, radius=min(line1_len, line2_len)/5).set_color(color)
        angle_helper = Angle(line1=line1, line2=line2, radius=0).set_color(color)
        q1 = angle.points #  save all coordinates of points of angle a1
        q2 = angle_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)]) 
        mfill = VMobject().set_color(color)
        mfill.set_points_as_corners(pnts).set_fill(color, opacity=1)


        if rotate:
            # get common point
            common_points = Intersection(line1, line2)
            # common_point = common_points[0]
            # elif all(line1.start) == all(line2.end):
            #     common_point = line1.start
            # elif all(line1.end) == all(line2.start):
            #     common_point = line1.end
            # elif all(line1.end) == all(line2.end):
            #     common_point = line1.end
            mfill.rotate(angle=rotate_for, about_point=about_point)
            

        return mfill