from manim import *
from manim.utils.color import Color   
from modules import Proposition as p
from Book_I_Definitions import Book_I_Definitions

class Book_I_Postulates(Scene):
    
    def construct(self):
        
        # Display first definition

        Definicija_I = "Knjiga I, Postulat I."
        prop = f'Da se od vsake točke do vsake druge lahko potegne daljica (premica, ravna črta).'
        
        p.display_text(self, Definicija_I, prop)

        line = Book_I_Postulates.Postulate_I(scene=self, point_1 = 2*LEFT+DOWN, point_2 = 2*RIGHT+UP)
        self.wait()

        self.clear()
        
        # Display first definition

        Definicija_II = "Knjiga I, Postulat II."
        prop = f'Da se omejena daljica (premica, ravna črta)\nlahko neprekinjeno (povezano) podaljša\nv svoji premici (daljici, ravni črti).'
        
        p.display_text(self, Definicija_II, prop)

        extended_line = Book_I_Postulates.Postulate_II(self, line, to_exend = "end", extension_length = 3)
        self.wait()

        self.clear()
        
        # Display the third postlate
        
        Definicija_III = "Knjiga I, Postulat III."
        prop = f'Da se z vsakim središčem in z vsako razdaljo lahko opiše krog.'
        
        p.display_text(self, Definicija_III, prop)

        circle = Book_I_Postulates.Postulate_III(self, center=DOWN, radius=2.)
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
        angle2.set_color(RED)
        self.play(Create(angle1))
        self.play(Create(angle2))

        Book_I_Postulates.Postulate_IV(self, angle1, angle2)
        self.wait()

        self.clear()
        
        # Display the fifth postlate
        
        Definicija_V = "Knjiga I, Postulat V."
        prop = f'Da, če ena daljica (premica, ravna črta) v preseku z drugima dvema tvori na isti strani dva notranja kota,\nvsota katerih je manjša od dveh pravih kotov,\ntedaj se ti daljici (premici, ravnia ćrti), neomejeno (neskončno) podaljšani, sekata,\nin to na tisti strani, na kateri je vsota kotov manjša od dveh pravih.'
        
        line1 = Line(3*LEFT+2*UP, RIGHT+UP)
        line2 = Line(2*LEFT+3*DOWN, 2*RIGHT+UP)
        line3 = Line(2*LEFT+4*DOWN, LEFT+3*UP)
        
        Book_I_Postulates.Postulate_V(self, line1, line2, line3)
        
    def Postulate_I(scene : Scene, point_1, point_2, line_color=WHITE, point_1_color=WHITE, point_2_color=WHITE):
        line = Line(point_1, point_2, color=line_color)
        
        scene.add(Dot(point_1, color=point_1_color, z_index=100), Dot(point_2, color=point_2_color, z_index=100))
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
        
        scene.play(Create(Dot(center, color=color)))
        
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
        
        
    def Postulate_V(scene : Scene, line1 : Line, line2 : Line, line3 : Line):
        """
        And that if a straight-line falling across two (other) straight-lines 
        makes internal angles on the same side (of itself) less than two right-angles, 
        being produced to infinity, the two (other) straight-lines meet on that side (of the original straight-line) 
        that the (internal angles) are less than two right-angles (and do not meet on the other side).
        """
        
        if line1 not in scene.mobjects:
            scene.play(Create(line1))
            
        if line2 not in scene.mobjects:
            scene.play(Create(line2))
            
        if line3 not in scene.mobjects:
            scene.play(Create(line3))
            
        (angle1, value1) = Book_I_Definitions.Definition_IX(scene, line1, line3, create=False)
        if abs(value1) >= PI * (1/2):
            (angle1, value1)  = Book_I_Definitions.Definition_IX(scene, line1, line3, other_angle=True, create=False, quadrant=(1,-1))
        
        (angle2, value2) = Book_I_Definitions.Definition_IX(scene, line2, line3, create=False)
        if abs(value2) >= PI * (1/2):
            (angle2, value2) = Book_I_Definitions.Definition_IX(scene, line2, line3, other_angle=True, create=False)
        
        scene.play(Create(angle1))
        scene.play(Create(angle2))
        
        # scene.play(Transform(angle1.shift(-angle1.get_start())))
        # scene.play(Transform(angle2.shift(-angle2.get_start())))
    