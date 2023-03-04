import numpy as np
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        square = Square()
        square.set_fill(BLUE,opacity = 0.5)
        
        
        self.play(Create(square))  # show the circle on screen
        self.play(Transform(square,circle))
        self.play(FadeOut(square))
        
# class particle():
#     def __init__(self) -> None:
#         pass
# class Astral(particle):
    
#     def __init__(self,p):