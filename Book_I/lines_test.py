import pytest
from manim import *
from modules import Proposition as p

def test_do_lines_have_points_in_common():
    line_1 = Line(LEFT, RIGHT)
    line_2 = Line(RIGHT, LEFT)
    
    assert p.do_lines_have_common_points(line_1, line_2)
    
