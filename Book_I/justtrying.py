from manim import *

class JustTrying(Scene):
    def construct(self):

        line1 = Line(start=LEFT, end=RIGHT)
        line2 = Line(start=LEFT, end=UP)
        angle = Angle(line1, line2, color=WHITE)

        self.add(line1, line2, angle)
        print(angle.get_value() / DEGREES)