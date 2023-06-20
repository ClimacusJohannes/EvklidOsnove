import pytest
from manim import *
from modules import Proposition as p

def test_are_angles_congruent():
    line1 = Line(ORIGIN, RIGHT)
    line2 = Line(UP, ORIGIN)
    line1a = Line(RIGHT, ORIGIN)
    angle1 = Angle(line1, line2)
    angle2 = Angle(line1a, line2)
    
    assert p.are_angles_congruent(angle1, angle2)
    
