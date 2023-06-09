from Triangles import ScaleneTriangle
from manim import *

def test_triangle_heights():
    triangle = ScaleneTriangle(LEFT, RIGHT, UP)

    assert triangle.heights["Vc"] == 1