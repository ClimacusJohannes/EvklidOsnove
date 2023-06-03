from manim import *
from manim.utils.color import Color


from modules import Proposition as p

class Book_I_Definitions(Scene):

    def construct(self):

        # Display first definition

        Definicija_I = "Knjiga I, Definicija I."
        prop = "Točka je tisto, kar nima širine."
        
        p.display_text(self, Definicija_I, prop)

        point = Book_I_Definitions.Definition_I(self)
        self.wait()

        self.clear()

        # Display second definition

        Definicija_II = "Knjiga I, Definicija II."
        prop = "Črta/Daljica je dolžina brez širine."

        
        p.display_text(self, Definicija_II, prop)

        line = Book_I_Definitions.Definition_II(self)
        self.wait()

        self.clear()

        # Display second definition

        Definicija_II = "Knjiga I, Definicija III."
        prop = "Konca daljice sta točki."

        
        p.display_text(self, Definicija_II, prop)

        Book_I_Definitions.Definition_III(self, line)
        self.wait()

        self.clear()

        # Display fourth definition

        Definicija_II = "Knjiga I, Definicija IV."
        prop = "Ravna črta leži enakomerno\nmed svojima koncema."

        
        p.display_text(self, Definicija_II, prop)

        Book_I_Definitions.Definition_IV(self, point1=line.start, point2=line.end)
        self.wait()

        self.clear()

        # Display fifth definition

        Definicija_V = "Knjiga I, Definicija V."
        prop = "Ploskev ima samo dolžino in širino."

        
        p.display_text(self, Definicija_V, prop)

        line1 = Book_I_Definitions.Definition_II(self)
        line2 = Book_I_Definitions.Definition_II(self, start=line.start, end=3*UP)

        Book_I_Definitions.Definition_V(self, [line1, line2])
        self.wait()

        self.clear()

        # Display the sixth definition

        Definicija_VI = "Knjiga I, Definicija VI."
        prop = "Konci ravnine so daljice."

        p.display_text(self, Definicija_VI, prop)
        self.wait()

        self.clear()

        

        Book_I_Definitions.Definition_VI(self)
        self.wait()

        self.clear()


    def Definition_I(scene : Scene, point : Point = ORIGIN, color : Color = WHITE):
        """
        "First Definition: A point is that which has not parts"
        Takes in a scene : Scene, a point : Point and color : Color
        Plays the creation of a dot at the coordinates of the point
        """
        dot = Dot(point) 
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

    def Definition_III(scene : Scene, line : Line, first_dot_color = WHITE, second_dot_color = WHITE):
        """
        Third Definition: The extremities of a line are points.
        Takes in scene : Scene, line : Line, and first_dot_color and second_dot_color : Color
        Plays the creation of a line from start to end
        """
        # construct dots at the ends of the line
        dot1 = Dot(line.start, color=line.color)
        dot2 = Dot(line.end, color=line.color)

        scene.add(line)
        scene.play(Create(dot1))
        scene.play(Create(dot2))

        line.add(dot1)
        line.add(dot2)

        return line
    
    def Definition_IV(scene : Scene, point1 : Point, point2 : Point, color : Color = WHITE):
        """
        "Fourth Definition: A straight line is that which lies evenly between its extremities."
        Takes in (a) scene : Scene, (b) point1 and (c) point2 : Point, color : Color 
        Plays the creation of two point at the extremities of the line.
        """
        dot1 = Dot(point1, color=color)
        dot2 = Dot(point2, color=color)
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


        # add the fourth vertex

        forth_corner = 0
        end = 0
        points_in_common = (p, which)
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
        # corners.append(forth_corner)
        # corners.append(end)

        # i = 0
        # j = 0
        # while i < len(corners):
        #     j = i + 1
        #     while j < len(corners):
        #         count = 0
        #         k = 0
        #         while k < len(corners[i]):
        #             if corners[i][count] == corners[j][count]:
        #                 count += 1
        #             k += 1
        #         if count == 3:
        #             corners.pop(j)
        #         j += 1
        #     i += 1
                    

        print(corners)
        surface = Polygram(corners, color=YELLOW, fill_color=YELLOW)
        surface = Polygon(*corners, color=YELLOW, fill_color=YELLOW)

        scene.add(line_1, line_2)
        scene.wait()
        scene.play(Create(surface))

        return 

    def Definition_VI(scene : Scene, surface : Polygram = None):
        if not surface:
            surface = Rectangle(height=6, width=8, color=YELLOW, fill_opacity=0.5, stroke_opacity=0.5)
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


    
