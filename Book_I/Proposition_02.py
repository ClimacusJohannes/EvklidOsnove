from manim import *
from numpy import matmul, ndarray, array, sqrt
import numpy as np
from modules import Proposition as p
from Proposition_01 import *

# config.background_color = '#fcf3d9'
class Proposition_II(Scene):
    def construct(self):

        title = 'Knjiga I, Izrek II'
        prop = 'Iz dane točke izriši\ndaljico enako dani daljici.'

        p.display_text(self, title, prop)

        dana_daljica = Line(start=  5 * LEFT + 2 * DOWN, end = 3 * LEFT + DOWN )
        dana_tocka = Dot(2 * LEFT + DOWN)

        self.play(Create(dana_daljica))
        self.play(Create(dana_tocka))

        Proposition_II.construction(self, dana_daljica, dana_tocka, initial_construction=True)

        # Dokaz
        podaljsana_daljica = self.mobjects[9]
        polmer_l = self.mobjects[10]
        koncna_daljica = self.mobjects[-1]
        koncna_daljica_copy=koncna_daljica.copy()
        self.add(koncna_daljica_copy)
        polmer_l.add(koncna_daljica)

        # self.play(Rotate(polmer_l, - (koncna_daljica.get_angle() - podaljsana_daljica.get_angle()), about_point=koncna_daljica.end))
        # self.play(Rotate(koncna_daljica, - (koncna_daljica.get_angle() - dana_daljica.get_angle()), about_point=dana_daljica.end))

    def construction(scene : Scene, dana_daljica : Line, dana_tocka : Dot, initial_construction : bool = False):
        initial_index = len(scene.mobjects)

        run_time=1.0
        lag_ratio=0.0
        if not initial_construction:
            run_time=0.3
            lag_ratio=0.0

        pomozna_daljica = DashedLine(start=dana_daljica.end, end=dana_tocka.get_arc_center())

        # Step one
        scene.play(Create(pomozna_daljica, run_time=run_time))
        scene.wait()

        # Step two
        (tocka_intersekcije, krak1, krog1, krak2, krog2) = Proposition_I_alt.construction(scene, pomozna_daljica, color=ORANGE, opposite_orientation=True)

        # Step three
        circle_s = Circle(radius=p.get_line_length(dana_daljica)).shift(dana_daljica.end).set_color(RED)
        p.rotate(circle_s)
        sredisce_s = Dot(circle_s.get_arc_center()).set_color(RED)
        polmer_s = Line(start=sredisce_s.get_arc_center(), end=(dana_daljica.end - (p.get_line_length(dana_daljica) * (-1) * p.get_line_slope(krak1)))).set_color(RED)
        scene.play(Create(sredisce_s, run_time=run_time))
        scene.play(Create(circle_s, run_time=run_time))

        podaljsana_daljica = Book_I_Postulates.Postulate_II(scene, krak1, retain = "start", extension_length=p.get_line_length(dana_daljica)).set_color(ORANGE)

        # podaljsaj enega izmed krakov
        scene.play(Create(polmer_s, run_time=run_time))
        scene.play(Transform(krak1, podaljsana_daljica, run_time=run_time))
        if initial_construction:
            scene.wait()


        circle_l = Circle(radius=p.get_line_length(podaljsana_daljica)).shift(podaljsana_daljica.start).set_color(ORANGE)
        sredisce_l = Dot(circle_l.get_arc_center(), z_index=101).set_color(ORANGE)
        scene.play(Create(sredisce_l, run_time=run_time))
        scene.play(Create(circle_l, run_time=run_time))

        polmer_l = p.create_extended_line(krak2, for_len=p.get_line_length(dana_daljica)).set_color(ORANGE)
        scene.play(Transform(krak2, polmer_l, run_time=run_time))
        koncna_daljica = Line(start=polmer_l.end, end=dana_tocka.get_arc_center()).set_color(BLUE)
        scene.play(Create(koncna_daljica), run_time=run_time)

        scene.wait(5)
        if not initial_construction:
            for object in scene.mobjects[initial_index:-1]:
                try:
                    scene.remove(object)
                except:
                    pass
            scene.wait()
