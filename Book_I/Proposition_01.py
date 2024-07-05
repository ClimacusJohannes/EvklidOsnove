from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np

from modules import *
from Book_I_Postulates import Book_I_Postulates
from Book_I_Definitions import Book_I_Definitions

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

        steps = Mobject()

        # KONSTRUKCIJA

        down_shift = 0
        step = Proposition.display_step(scene, "KONSTRUKCIJA")
        steps.add(step)
        down_shift += (((step.height + 0.2))  * DOWN)

        step = Proposition.display_step(scene, f'1) Izriši <span fgcolor="{RED}">⨀</span> s središčem <span fgcolor="{RED}">●</span>\nin polmerom <span font-weight="700" fgcolor="{BLUE}">⎯</span>\n - Tretji postulat.', down_shift)
        steps.add(step)
        krog1 = Book_I_Postulates.Postulate_III(scene, daljica.start, daljica_length, color=RED)
        down_shift += (((step.height + 0.2))  * DOWN)

        step = Proposition.display_step(
                scene,
                f'2) Izriši <span fgcolor="{GREEN}">⨀</span> s središčem <span fgcolor="{GREEN}">●</span>\nin polmerom <span fgcolor="{BLUE}">⎯</span>\n - Tretji postulat.\n',
                down_shift,
                prev_step=step)
        steps.add(step)
        krog2 = Book_I_Postulates.Postulate_III(scene, daljica.end, daljica_length, color=GREEN)
        down_shift += (((step.height + 0.2))  * DOWN)

        step = Proposition.display_step(scene, f'3) Iz točke ●,v kateri se\nizrisana kroga sekata,\nizriši dve ravni daljici ⎯ in  ⎯,\nki se končata v točkah <span fgcolor="{RED}">●</span> and <span fgcolor="{GREEN}">●</span>\n - Prvi Postulat', down_shift, prev_step=step)
        steps.add(step)
        tocka_intersekcije = ( daljica.start + ( (daljica_length / 2) * (daljica_slope))) + ((matmul(daljica_slope, array([[0,-1,0],[1,0,0],[0,0,0]])) * (daljica_length * sqrt(3) / 2)) * orientation)
        krak1 = Book_I_Postulates.Postulate_I(scene, point_1=tocka_intersekcije, point_2=daljica.start, point_2_color=RED, line_color=RED)
        krak2 = Book_I_Postulates.Postulate_I(scene, point_1=tocka_intersekcije, point_2=daljica.end,  point_2_color=GREEN, line_color=GREEN)
        down_shift += ((step.height + 0.2)  * DOWN)

        # '

        for o in steps.submobjects:
            scene.play(Uncreate(o, run_time=run_time))


        # DOKAZ

        down_shift = 0
        step = Proposition.display_step(scene, "DOKAZ")
        steps.add(step)
        down_shift += (((step.height + 0.2))  * DOWN)

        step = Proposition.display_step(scene, f'1) <span color="{BLUE}">⎯</span> = <span color="{RED}">⎯</span>, \n - 15. Definicija', down_shift=down_shift, prev_step=step)
        steps.add(step)
        (k, d) = Book_I_Definitions.Definition_XV(scene, krog1, line1=daljica, line2=krak1)
        scene.wait(1.3)
        scene.play(Uncreate(d))
        down_shift += ((step.height + 0.2) * DOWN)

        step = Proposition.display_step(scene, f'2) <span color="{BLUE}">⎯</span> = <span color="{GREEN}">⎯</span> \n 15.Definicija', down_shift=down_shift, prev_step=step)
        steps.add(step)
        (k, d) = Book_I_Definitions.Definition_XV(scene, krog2, line1=daljica, line2=krak2, rotation=True)
        scene.wait(1.3)
        scene.play(Uncreate(d))
        down_shift += ((step.height + 0.2) * DOWN)

        step = Proposition.display_step(scene,
                                        f'3)  <span color="{RED}">⎯</span> =  <span color="{GREEN}">⎯</span>.\n QED.',
                                        down_shift=down_shift,
                                        prev_step=step)

        scene.remove()

        if not initial_construction:
            scene.play(Uncreate(krog1, run_time=run_time, lag_ratio=lag_ratio))
            scene.play(Uncreate(krog2, run_time=run_time, lag_ratio=lag_ratio))
            scene.wait()
