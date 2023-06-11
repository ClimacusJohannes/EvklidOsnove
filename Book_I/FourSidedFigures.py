from manim import *
from manim.utils.color import Color

class Rhombus(Polygon):
    def __init__(self, side_len=2.5, alpha=PI*(1/3), **kwargs):
        self.side_len = side_len
        self.alpha = alpha
        self.vertices = [
            [0, 0, 0],
            [side_len, 0, 0],
            [side_len + self.side_len*np.cos(self.alpha),
            self.side_len*np.sin(self.alpha),  
            0],
            [self.side_len*np.cos(self.alpha),
            self.side_len*np.sin(self.alpha),  
            0],
            [0, 0, 0]
        ]
        print(self.vertices)
        super().__init__(*self.vertices, **kwargs)

        
        