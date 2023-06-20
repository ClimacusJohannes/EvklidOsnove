from Triangles import EuclidTriangle, RightAngledTriangle
from manim import *
import pytest


def test_triangle_heights():
    triangle = EuclidTriangle(LEFT, RIGHT, UP)

    assert triangle.heights["Vc"] == 1

def test_triangle_angles():
    triangle = EuclidTriangle(LEFT, RIGHT, UP)

    sum = 0
    for angle in ["alpha", "beta", "gamma"]:
        sum += triangle.angles[angle]
    s = PI / DEGREES
    assert abs(sum) == s

def test_right_triangle_beta():
    triangle = EuclidTriangle(LEFT, RIGHT, RIGHT+UP)
    angle = (PI/2) / DEGREES
    assert triangle.angles["beta"] == angle

def test_right_triangle_alpha():
    triangle = EuclidTriangle(LEFT, RIGHT, LEFT+UP)
    angle = (PI/2) / DEGREES
    assert triangle.angles["alpha"] == angle

def test_right_triangle_gamma():
    triangle = EuclidTriangle(LEFT, UP+RIGHT, LEFT+UP)
    angle = (PI/2) / DEGREES
    assert triangle.angles["gamma"] == angle

def test_right_triangle():
    triangle = RightAngledTriangle(LEFT, RIGHT, RIGHT+UP)
    right_angle = (PI/2) / DEGREES
    assert triangle.angles["gamma"] == right_angle

# # @pytest.mark.fake
# def test_fake_right_triangle():
#     triangle = RightAngledTriangle(2*LEFT, 2*RIGHT, 1/2*UP)
#     right_angle = (PI/2) / DEGREES
#     assert triangle.angles["gamma"] == right_angle

# assert exc_info.message == "This is not a right triangle"
def test_fake_right_triangle():
    with pytest.raises(ValueError):
        triangle = RightAngledTriangle(2*LEFT, 2*RIGHT, RIGHT+UP)
        print(triangle.angles["gamma"])

# assert exc_info.message == "This is not a right triangle"
