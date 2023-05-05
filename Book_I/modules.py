from manim import *
import numpy as np

class Proposition():
    def display_text(scene : Scene, title: str, prop: str): 
        scene.play(Create(title))
        scene.wait()
        scene.remove(title)
        scene.play(Create(prop))
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
