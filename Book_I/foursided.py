from manim import *

from FourSidedFigures import Rhombus

class Example(Scene):
    def construct(self):
        rhombus = Rhombus()
        self.add(rhombus)
        self.wait()