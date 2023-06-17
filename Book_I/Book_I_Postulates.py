from manim import *
from manim.utils.color import Color   
from modules import Proposition as p
from Book_I_Definitions import Book_I_Definitions

class Book_I_Propositions(Scene):
    
    def construct(self):
        
        # Display first definition

        Definicija_I = "Knjiga I, Postulat I."
        prop = f'Da se od vsake točke do vsake druge lahko potegne daljica (premica, ravna črta).'
        
        p.display_text(self, Definicija_I, prop)

        line = Book_I_Propositions.Postulate_I(scene=self, point_1 = 2*LEFT+DOWN, point_2 = 2*RIGHT+UP)
        self.wait()

        self.clear()
        
        # Display first definition

        Definicija_II = "Knjiga I, Postulat II."
        prop = f'Da se omejena daljica (premica, ravna črta)\nlahko neprekinjeno (povezano) podaljša\nv svoji premici (daljici, ravni črti).'
        
        p.display_text(self, Definicija_II, prop)

        extended_line = Book_I_Propositions.Postulate_II(self, line, to_exend = "end", extension_length = 3)
        self.wait()

        self.clear()
        
        # Display the third postlate
        
        Definicija_III = "Knjiga I, Postulat III."
        prop = f'Da se z vsakim središčem in z vsako razdaljo lahko opiše krog.'
        
        p.display_text(self, Definicija_III, prop)

        circle = Book_I_Propositions.Postulate_III(self, center=DOWN, radius=2.)
        self.wait()

        self.clear()
        
        # Display the fourth postlate
        
    def Postulate_I(scene : Scene, point_1, point_2):
        line = Line(point_1, point_2)
        
        scene.add(Dot(point_1), Dot(point_2))
        scene.play(Create(line))
        return line
        
    def Postulate_II(scene : Scene, line : Line, to_exend : str = "end", extension_length = 1):
        
        if line not in scene.mobjects:
            scene.play(Create(line))
        
        
        extended_line = None
        start, end = ORIGIN, ORIGIN
        line_slope = p.get_line_slope(line)
        
        if to_exend == "start":
            end = line.end
            
            start = line.start + extension_length * line_slope
            extended_line = Line(start=start, end=end)
            if p.get_line_length(extended_line) < p.get_line_length(line):
                start = line.start - extension_length * line_slope
                extended_line = Line(start=start, end=end)
        
        elif to_exend == "end":
            start = line.start
            
            end = line.end + extension_length * line_slope
            extended_line = Line(start=start, end=end)
            if p.get_line_length(extended_line) < p.get_line_length(line):
                end = line.end - extension_length * line_slope
                extended_line = Line(start=start, end=end)
                
        else:
            raise ValueError("to_exend must be 'start' or 'end'")
        

        scene.play(Transform(line, extended_line))
        
        return extended_line

    def Postulate_III(scene : Scene, center : Point, radius : float = 1., color : Color = RED):
        
        scene.add(Dot(center))
        
        circle = Circle(arc_center=center, radius=radius, color=color)
        
        scene.play(Create(circle))
        
        return circle