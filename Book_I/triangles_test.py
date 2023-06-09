from Triangles import ScaleneTriangle
from manim import *

def test_triangle_heights():
    triangle = ScaleneTriangle(LEFT, RIGHT, UP)

    assert triangle.heights["Vc"] == 1

def test_triangle_angles():
    triangle = ScaleneTriangle(LEFT, RIGHT, UP)

    sum = 0
    for angle in ["alpha", "beta", "gamma"]:
        sum += triangle.angles[angle]
    s = PI / DEGREES
    assert abs(sum) == s

def test_right_triangle_beta():
    triangle = ScaleneTriangle(LEFT, RIGHT, RIGHT+UP)
    angle = (PI/2) / DEGREES
    assert triangle.angles["beta"] == angle

def test_right_triangle_alpha():
    triangle = ScaleneTriangle(LEFT, RIGHT, LEFT+UP)
    angle = (PI/2) / DEGREES
    assert triangle.angles["alpha"] == angle

def test_right_triangle_gamma():
    triangle = ScaleneTriangle(LEFT, UP+RIGHT, LEFT+UP)
    angle = (PI/2) / DEGREES
    assert triangle.angles["gamma"] == angle
