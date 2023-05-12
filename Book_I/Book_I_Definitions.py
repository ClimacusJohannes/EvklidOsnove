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
        """
        dot1 = Dot(point1, color=color)
        dot2 = Dot(point2, color=color)
        line = Line(start=point1, end=point2)

        scene.add(dot1)
        scene.add(dot2)
        scene.play(Create(line))

        line.add(dot1)
        line.add(dot2)

        return line
    
    def Definition_V():
        """
        Fifth definition: A surface is that which has length and breadth only.
        """