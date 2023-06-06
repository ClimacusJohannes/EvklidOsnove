from manim import *
from manim.utils.color import Color


from modules import Proposition as p

class Book_I_Definitions(Scene):

    def construct(self):

        # Display first definition

        Definicija_I = "Knjiga I, Definicija I."
        prop = f'<span fgcolor="{YELLOW}">Točka</span> je tisto, kar nima delov/ni deljivo.'
        
        p.display_text(self, Definicija_I, prop)

        point = Book_I_Definitions.Definition_I(self, color=YELLOW)
        self.wait()

        self.clear()

        # Display second definition

        Definicija_II = "Knjiga I, Definicija II."
        prop = f'<span fgcolor="{RED}">Črta/Daljica</span> je dolžina brez širine.'

        
        p.display_text(self, Definicija_II, prop)

        line = Book_I_Definitions.Definition_II(self, color=RED)
        self.wait()

        self.clear()

        # Display second definition

        Definicija_II = "Knjiga I, Definicija III."
        prop = f'Konca daljice sta <span fgcolor="{YELLOW}">točki</span>.'

        
        p.display_text(self, Definicija_II, prop)

        Book_I_Definitions.Definition_III(self, line, dot_color=YELLOW)
        self.wait()

        self.clear()

        # Display fourth definition

        Definicija_II = "Knjiga I, Definicija IV."
        prop = f'<span fgcolor="{BLUE}">Ravna črta</span> je tisto, kar leži enakomerno\nmed svojima koncema - <span fgcolor="{YELLOW}">točkama</span>. \n (<span fgcolor="{BLUE}">Ravna črta</span> (premica, ali daljica) je tista, ki enako leži za točke na njej.)'

        
        p.display_text(self, Definicija_II, prop)

        Book_I_Definitions.Definition_IV(self, point1=line.start, point2=line.end, color=BLUE, dot_color=YELLOW)
        self.wait()

        self.clear()

        # Display fifth definition

        Definicija_V = "Knjiga I, Definicija V."
        prop = "Površina ima samo dolžino in širino."

        
        p.display_text(self, Definicija_V, prop)

        line1 = Book_I_Definitions.Definition_II(self)
        line2 = Book_I_Definitions.Definition_II(self, start=line.start, end=3*UP)

        Book_I_Definitions.Definition_V(self, [line1, line2])
        self.wait()

        self.clear()

        # Display the sixth definition

        Definicija_VI = "Knjiga I, Definicija VI."
        prop = f'Konci <span fgcolor="{YELLOW}">površine</span> so <span fgcolor="{RED}">daljice</span>.'

        p.display_text(self, Definicija_VI, prop)
        

        Book_I_Definitions.Definition_VI(self)
        self.wait()

        self.clear()

        # .....

        # Display the ninth definition

        Definicija_IX = "Knjiga I, Definicija IX."
        prop = f'Če sta črti <span fgcolor="{RED}">|</span> <span fgcolor="{BLUE}">|</span>, ki tvorita kot, ravni, pravimo, da je kot ravnolinijski (premočrtni).'

        p.display_text(self, Definicija_IX, prop)
        
        line_1 = Line(start=2*LEFT+DOWN, end=2*RIGHT+DOWN, color=RED, z_index = 1)
        line_2 = Line(start=2*LEFT+DOWN, end=1.5*RIGHT + UP, color=BLUE, z_index = 1)

        Book_I_Definitions.Definition_IX(self, line_1, line_2)
        self.wait()

        self.clear()

        # Display the tenth definition

        Definicija_X = "Knjiga I, Definicija X"
        prop = f'Če daljica/premica, ki stoji na drugi,\ntvori z njo dva sosednja <span fgcolor="{BLUE}">enaka kota, vsaki izmed njiju je pravi</span>,\nin stoječa daljica/premica se imenuje spuščena (pravokotnica, normala) na tisto na kateri stoji.'

        p.display_text(self, Definicija_X, prop)

        line_1_a = Line(start=2*LEFT+2*DOWN, end=2*DOWN)
        line_1_a.z_index = 1
        line_1_b = Line(start=2*DOWN, end=2*RIGHT+2*DOWN)
        line_1_b.z_index = 1
        line_2 = Line(start=ORIGIN, end=2*DOWN)
        line_2.z_index = 1

        Book_I_Definitions.Definition_X(self, line_1_a, line_1_b, line_2)
        self.wait()

        self.clear()

        # Display the eleventh definition

        Definicija_X = "Knjiga I, Definicija XI"
        prop = f'<span fgcolor="{RED}">Topi kot</span> je tisti, ki je veˇcji od pravega.'

        p.display_text(self, Definicija_X, prop)

        line_1 = Line(start=2*DOWN, end=3*RIGHT+2*DOWN, color=BLUE)
        line_2 = Line(start=line_1.start, end=line_1.end, color=YELLOW).rotate(angle = (3 / 4) * PI, about_point=line_1.start)
        line_1.z_index = 1
        line_2.z_index = 1

        Book_I_Definitions.Definition_XI(self, line_1, line_2)
        self.wait()

        self.clear()

    def Definition_I(scene : Scene, point : Point = ORIGIN, color : Color = WHITE):
        """
        "First Definition: A point is that which has not parts"
        Takes in a scene : Scene, a point : Point and color : Color
        Plays the creation of a dot at the coordinates of the point
        """
        dot = Dot(point, color=color) 
        scene.play(Create(dot))

        return dot

    def Definition_II(scene : Scene, start : Point = 2 * LEFT, end : Point = 2 * RIGHT, color : Color = WHITE):
        """
        Second Definition: A line is length without breath.
        Takes in scene : Scene, start and end of line : Point, and color : Color
        Plays the creation of a line from start to end
        """
        line = Line(start=start, end=end, color=color)
        scene.play(Create(line))

        return line

    def Definition_III(scene : Scene, line : Line, first_dot_color = WHITE, second_dot_color = WHITE, dot_color = None):
        """
        Third Definition: The extremities of a line are points.
        Takes in scene : Scene, line : Line, and first_dot_color and second_dot_color : Color
        Plays the creation of a line from start to end
        """
        if not dot_color:
            dot_color = line.color
        # construct dots at the ends of the line
        dot1 = Dot(line.start, color=dot_color)
        dot2 = Dot(line.end, color=dot_color)

        scene.add(line)
        scene.play(Create(dot1))
        scene.play(Create(dot2))

        line.add(dot1)
        line.add(dot2)

        return line
    
    def Definition_IV(scene : Scene, point1 : Point, point2 : Point, color : Color = WHITE, dot_color = None):
        """
        "Fourth Definition: A straight line is that which lies evenly between its extremities."
        Takes in (a) scene : Scene, (b) point1 and (c) point2 : Point, color : Color 
        Plays the creation of two point at the extremities of the line.
        """

        if not dot_color:
            dot_color = color

        dot1 = Dot(point1, color=dot_color)
        dot2 = Dot(point2, color=dot_color)
        line = Line(start=point1, end=point2, color=color)

        scene.add(dot1)
        scene.add(dot2)
        scene.play(Create(line))

        line.add(dot1)
        line.add(dot2)

        return line
    
    def Definition_V(scene : Scene, lines : list[Line]):
        """
        Fifth definition: A surface is that which has length and breadth only.
        Takes in (1) scene : Scene, (2) line_1 : Line, (3) line_2 : Line
        Plays the creation of a plane surface - a polygon from two lines
        """
        for line in lines:
            line_1 = lines[lines.index(line)]
            try:
                line_2 = lines[lines.index(line)+1]
            except:
                line_2 = lines[0]
            (points_in_common, which) = p.do_lines_have_common_points(line_1, line_2)
            if len(points_in_common) == 0:
                ValueError("the lines have to have one extremity in common!")
            if (line_1.get_angle() == line_2.get_angle()):
                ValueError("the lines should not be parallel!")
            
        corners = []


        # add the vertexes

        if which == "start-start":
            corners.append(line_1.start)
            corners.append(line_1.end)
            corners.append(line_2.end + (line_1.end - line_1.start))
            corners.append(line_2.end)
            corners.append(line_1.start)
        elif which == "start-end":
            corners.append(line_1.start)
            corners.append(line_1.end)
            corners.append(line_2.start + (line_1.end - line_1.start))
            corners.append(line_2.start)
            corners.append(line_1.start)
        elif which == "end-start":
            corners.append(line_1.end)
            corners.append(line_1.start)
            corners.append(line_2.end + (line_1.start - line_1.end))
            corners.append(line_2.end)
            corners.append(line_2.start)
        elif which == "end-end":
            corners.append(line_1.end)
            corners.append(line_1.start)
            corners.append(line_2.start + (line_1.start - line_1.end))
            corners.append(line_2.start)
            corners.append(line_2.end)
        
        print(corners)
        surface = Polygon(*corners, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)

        scene.add(line_1, line_2)
        scene.wait()
        scene.play(Create(surface))

        return surface

    def Definition_VI(scene : Scene, surface : Polygram = None):
        """
        Sixth definition: The extremities of a surface are lines.
        Takes in (a) Scene and (b) a surface : Polygon
        Plays the creation of lines (Book I, Definition IV) at the extremities of the given surface.
        """
        if not surface:
            surface = Rectangle(height=3, width=4, color=YELLOW, fill_opacity=0.5, stroke_opacity=0.5).shift(RIGHT+DOWN)
            scene.add(surface)
            scene.wait()

        points = surface.get_vertices()
        lines = VGroup()

        i = 0
        while i < len(points):
            Book_I_Definitions.Definition_IV(scene, points[i-1], points[i], color=RED)
            # line = Line(start=points[i-1], end=points[i], color=GREEN)
            # lines.add(line)
            scene.wait(0.5)
            i += 1

        scene.play(Create(lines))

        return lines
    
    def Definition_IX(scene : Scene, line_1 : Line, line_2 : Line, color : Color = YELLOW, other_angle : bool = False, angle_radius : int | float = 4, quadrant=(1,1)):
        """
        Ninth definition:
        And when the lines containing the angle are straight then the angle is called rectilinear.
        Takes in (a) scene : Scene and two lines: (b) line_1 : Line, (c) line_2 : Line, (d) other_angle : bool and (e) angle_radius : float.
        Angle radius is calculated as radius=min(line_1_len, line_2_len)/angle_radius.
        Plays the creation of an angle between two lines.
        """

    
        line_1_len = p.get_line_length(line_1)
        line_2_len = p.get_line_length(line_2)
        
        # create an angle with radius
        angle = Angle(line1=line_1, line2=line_2, radius=min(line_1_len, line_2_len)/angle_radius, other_angle=other_angle, quadrant=quadrant).set_color(color)
        # crate an angle without a radiua
        angle_helper = Angle(line1=line_1, line2=line_2, radius=0, other_angle=other_angle, quadrant=quadrant).set_color(color)
        
        q1 = angle.points #  save all coordinates of points of angle a1
        q2 = angle_helper.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        
        # concatenate both sets of points
        pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)]) 

        # crate an VMobject using the concatenadet sets of points as corners
        mfill = VMobject().set_color(color)
        mfill.set_points_as_corners(pnts).set_fill(color, opacity=0.5)


        # If the user wants to rotate, then rotate
        # if rotate:
        #     # get common point
        #     common_points = Intersection(line_1, line2)
        #     # common_point = common_points[0]
        #     # elif all(line1.start) == all(line2.end):
        #     #     common_point = line1.start
        #     # elif all(line1.end) == all(line2.start):
        #     #     common_point = line1.end
        #     # elif all(line1.end) == all(line2.end):
        #     #     common_point = line1.end
        #     mfill.rotate(angle=rotate_for, about_point=about_point)

        scene.add(line_1, line_2)
        scene.play(Create(mfill))
            
        return mfill

    def Definition_X(scene: Scene, line_1 : Line, line_2 : Line, line_3 : Line = None):
        """
        Byrne: When one straight line standing on another straight line makes the adjacent angles equal,
        each of these angles is called a right angle, and each of these lines is said to be perpendicular to the other.
        Takes in (a) scene : Scene,
        Two options (1) (b) line_1, (c) line_2, where line_1 and line_2 have one point in common.
        Or (2) (b) (line_1), (c) line_2, (d) line_3, where line_1, _2, and _3 have one of the points the same.
        
        Euclid: And when a straight-line stood upon (another) straight-line makes adjacent angles 
        (which are) equal to one another, each of the equal angles is a right-angle,
        and the former straight- line is called perpendicular to that upon which it stands.
        """

        common_point = 0

        if not (line_3):
            pass # to be implemented later
        else:
            if p.are_points_equal(p.do_lines_have_common_points(line_1=line_1, line_2=line_2)[0], p.do_lines_have_common_points(line_1=line_1, line_2=line_3)[0]):
                commmon_point = p.do_lines_have_common_points(line_1=line_1, line_2=line_2)[0]
            else:
                ValueError("The lines have to have a point in common");
        
        _line_1= Line()
        if p.are_points_equal(common_point, line_1.start):
            _line_1 = line_1
        else:
            _line_1 = Line(start=commmon_point, end=line_1.end)
        
        _line_2= Line()
        if p.are_points_equal(common_point, line_2.start):
            _line_2 = line_2
        else:
            _line_2 = Line(start=commmon_point, end=line_2.end)

        _line_3= Line()
        if p.are_points_equal(common_point, line_3.start):
            _line_3 = line_3
        else:
            _line_3 = Line(start=commmon_point, end=line_3.end)

        scene.add(line_1, line_2, line_3)

        angle1 = Book_I_Definitions.Definition_IX(scene=scene, line_1=line_1, line_2=line_3, color=BLUE, angle_radius=2., other_angle=True, quadrant=(-1,-1))
        angle2 = Book_I_Definitions.Definition_IX(scene=scene, line_1=line_2, line_2=line_3, color=BLUE, angle_radius=2., other_angle=False, quadrant=(1,-1))
        # scene.play(Create(angle1))
        # scene.play(Create(angle2))

    def Definition_XI(scene : Scene, line_1 : Line, line_2 : Line):

        if abs(line_1.get_angle() - line_2.get_angle()) < (PI * (1/2)):
            ValueError("The angle between the lines has to be larger than a right angle.")

        if not (line_1 in scene.mobjects):
            scene.add(line_1)
        if not (line_2 in scene.mobjects):
            scene.add(line_2)

        angle = Book_I_Definitions.Definition_IX(scene, line_1, line_2, color=RED)

        return angle