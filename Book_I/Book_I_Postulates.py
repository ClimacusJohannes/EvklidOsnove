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
        
        Definicija_IV = "Knjiga I, Postulat IV."
        prop = f'Da so vsi pravi koti med sabo enaki.'
        
        p.display_text(self, Definicija_IV, prop)
        
        lines1 = (Line(2*RIGHT, RIGHT), Line(RIGHT, RIGHT+UP))
        lines2 = (Line(2*LEFT, LEFT), Line(LEFT, LEFT+UP))
        
        angle1 = Angle(line1=lines1[0], line2=lines1[1], radius=0.5, other_angle=False, quadrant=(-1, 1))
        angle2 = Angle(line1=lines2[0], line2=lines2[1], radius=0.5, other_angle=True, quadrant=(-1, 1))
        
        for line in lines1:
            angle1.add(line)
        for line in lines2:
            angle2.add(line)
        self.play(Create(angle1))
        self.play(Create(angle2))

        Book_I_Propositions.Postulate_IV(self, angle1, angle2)
        self.wait()

        self.clear()
        
        # Display the fifth postlate
        
        Definicija_V = "Knjiga I, Postulat V."
        
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
    
    def Postulate_IV(scene : Scene, angle_1 : Angle, angle_2 : Angle):
        
        if angle_1 not in scene.mobjects:
            scene.play(Create(angle_1))
        if angle_2 not in scene.mobjects:
            scene.play(Create(angle_2))
        
        if abs(angle_1.get_value()) != PI * (1/2):
            raise ValueError("angle_1 must be a right angle, but is " + str(angle_1.get_value())+ "\nTry ather_angle=True")
        elif abs(angle_2.get_value()) != PI * (1/2):
            raise ValueError("angle_2 must be a right angle, but is " + str(angle_2.get_value()) + "\nTry ather_angle=True")
        
        (angle_1_center, _nn) = p.do_lines_have_common_points(line_1=angle_1.get_lines()[0], line_2=angle_1.get_lines()[1])
        (angle_2_center, _nn) = p.do_lines_have_common_points(line_1=angle_2.get_lines()[0], line_2=angle_2.get_lines()[1])
        
        # center1 = Dot(angle_1_center)
        # angle_1.add(center1)
        # center2 = Dot(angle_2_center)
        # angle_2.add(center2)
        
        scene.play(angle_1.animate.shift(-angle_1_center))
        scene.play(angle_2.animate.shift(-angle_2_center))
        
        rotate_for = p.rotate_to_cover_other_angle(angle_1, angle_2)
        
        print("Rotating for " + str(rotate_for))
        scene.play(Rotate(angle_2, angle=rotate_for, about_point=ORIGIN))
        
        
        
        
        
        
            