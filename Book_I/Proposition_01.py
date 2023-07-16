from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np

from modules import *
from Book_I_Postulates import Book_I_Postulates


class Proposition_I(Scene):
    def construct(self):
        
        # define all the variables

        title = "Knjiga I, Izrek I"
        prop = "Na dani daljici\nizriši enakostranični trikotnik."

        Proposition.display_text(self, title, prop)

        daljica = Line(start=LEFT, end=RIGHT)


        self.play(Create(daljica))
        self.wait()

        Proposition_I.construction(self, daljica, initial_construction=True, oposite_orientation = True)

    def construction(scene : Scene, daljica : Line, color : str = WHITE, initial_construction : bool = False, oposite_orientation : bool=False):

        run_time=1.0
        lag_ratio=0.0
        if not initial_construction:
            run_time=0.3
            lag_ratio=0.0

        orientation = 1
        if oposite_orientation:
            orientation = -1

        daljica_length = np.linalg.norm(daljica.end - daljica.start)
        daljica_slope = (daljica.end - daljica.start) / np.linalg.norm(daljica.end - daljica.start)

        tocka_intersekcije = ( daljica.start + ( (daljica_length / 2) * (daljica_slope))) + ((matmul(daljica_slope, array([[0,-1,0],[1,0,0],[0,0,0]])) * (daljica_length * sqrt(3) / 2)) * orientation)
        
        krog1 = Circle.from_three_points(daljica.start - (daljica_length * daljica_slope), daljica.end, tocka_intersekcije).set_color(RED)
        scene.play(Create(krog1, run_time=run_time, lag_ratio=lag_ratio))
        if initial_construction:
            scene.wait()

        krog2 = Circle.from_three_points(daljica.start, daljica.end + (daljica_length * daljica_slope), tocka_intersekcije).set_color(BLUE)
        
        Proposition.rotate(krog2)

        scene.play(Create(krog2, run_time=run_time, lag_ratio=lag_ratio))
        if initial_construction:
            scene.wait()

        krak1 = Line(start=daljica.start, end=tocka_intersekcije)
        krak1.set_color(color)
        krak2 = Line(start=daljica.end, end=tocka_intersekcije)
        krak2.set_color(color)


        scene.play(Create(krak1, run_time=run_time, lag_ratio=lag_ratio))
        scene.play(Create(krak2, run_time=run_time, lag_ratio=lag_ratio))

        if initial_construction == False :
            scene.play(Uncreate(krog1, run_time=run_time, lag_ratio=lag_ratio))
            scene.play(Uncreate(krog2, run_time=run_time, lag_ratio=lag_ratio))
            scene.wait()

class Proposition_I_alt(Scene):
    def construct(self):
        
        # define all the variables

        title = "Knjiga I, Izrek I"
        prop = "Na dani daljici\nizriši enakostranični trikotnik."

        Proposition.display_text(self, title, prop)

        daljica = Book_I_Postulates.Postulate_I(self, point_1=3*LEFT+DOWN, point_2=LEFT+DOWN, line_color=BLUE, point_1_color=RED, point_2_color=GREEN)


        self.play(Create(daljica))
        self.wait()

        Proposition_I_alt.construction(self, daljica, initial_construction=True, opposite_orientation = True)

    def construction(scene : Scene, daljica : Line, color : str = WHITE, initial_construction : bool = False, opposite_orientation : bool=False):
        
        
        
        run_time=1.0
        lag_ratio=0.0
        if not initial_construction:
            run_time=0.3
            lag_ratio=0.0

        orientation = 1
        if opposite_orientation:
            orientation = -1
        
        daljica_length = np.linalg.norm(daljica.end - daljica.start)
        daljica_slope = (daljica.end - daljica.start) / np.linalg.norm(daljica.end - daljica.start)
        
        step_count = 0
        Proposition.display_step(scene, f'Let the <span font-size="300%" font-weight="700" fgcolor="{RED}">○</span>\nwith center <span fgcolor="{RED}">●</span> and radius <span font-weight="700" fgcolor="{BLUE}">⎯</span>\nhave been drawn - Postulate 3,', step_count)
        krog1 = Book_I_Postulates.Postulate_III(scene, daljica.start, daljica_length, color=RED)
        step_count += 2
        
        Proposition.display_step(scene, f'and again let the <span font-size="300%" font-weight="700" fgcolor="{GREEN}">○</span>\nwith center <span fgcolor="{GREEN}">●</span> and radius <span font-weight="700" fgcolor="{BLUE}">⎯</span>\nhave been drawn - Postulate 3.', step_count)
        krog2 = Book_I_Postulates.Postulate_III(scene, daljica.end, daljica_length, color=GREEN)
        step_count += 2
        
        Proposition.display_step(scene, f'And let the straight-lines ⎯ and ⎯ \nhave been joined from the point ●,\nwhere the circles cut one another,\n to the points <span fgcolor="{RED}">●</span> and <span fgcolor="{GREEN}">●</span> (respectively)\n- Postulate 1', step_count)
        tocka_intersekcije = ( daljica.start + ( (daljica_length / 2) * (daljica_slope))) + ((matmul(daljica_slope, array([[0,-1,0],[1,0,0],[0,0,0]])) * (daljica_length * sqrt(3) / 2)) * orientation)
        krak1 = Book_I_Postulates.Postulate_I(scene, point_1=tocka_intersekcije, point_2=daljica.start, point_2_color=RED)
        krak1.set_color(color)
        krak2 = Book_I_Postulates.Postulate_I(scene, point_1=tocka_intersekcije, point_2=daljica.end,  point_2_color=GREEN)
        krak2.set_color(color)

        if initial_construction == False :
            scene.play(Uncreate(krog1, run_time=run_time, lag_ratio=lag_ratio))
            scene.play(Uncreate(krog2, run_time=run_time, lag_ratio=lag_ratio))
            scene.wait()