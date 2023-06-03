from manim import *
import numpy as np

class Proposition():
    def display_text(scene : Scene, title: str, prop: str): 
        if (type(title) != Text) and type(title) == str:
            title = Text(title, font_size=DEFAULT_FONT_SIZE/1.2).to_edge(UL)
        else:
            TypeError('The title is supposed to be either a Text or a str.')
        if (type(prop) != Text) and type(prop) == str:
            prop = MarkupText(prop, font_size=title.font_size/1.5).to_edge(UL).shift(DOWN)
        else:
            TypeError('The prop is supposed to be either a Text or a str.')
        scene.play(Write(title))
        scene.wait()
        # scene.remove(title)
        scene.play(Write(prop))
        # scene.remove(prop)
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

    def do_lines_have_common_points(line_1, line_2):
        point_in_common = 0
        which_point = ""
        if (all(line_1.start) == all(line_2.start)):
            point_in_common = line_1.start
            which_point = "start-start"
        elif (all(line_1.start) == all(line_2.end)):
            point_in_common = line_1.start
            which_point = "start-end"
        elif (all(line_1.end) == all(line_2.start)):
            point_in_common = line_1.end 
            which_point = "end-start"
        elif (all(line_1.end) == all(line_2.end)):
            point_in_common = line_1.end
            which_point = "end-end"

        return (point_in_common, which_point)

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
        
        angle = Angle(line1=line1, line2=line2, radius=min(line1_len, line2_len)/5, other_angle=True).set_color(color)
        angle_helper = Angle(line1=line1, line2=line2, radius=0, other_angle=True).set_color(color)
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
    
