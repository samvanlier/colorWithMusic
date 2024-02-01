from line import Line
from splatter import Splatter
import logging

logger = logging.getLogger(__name__)

class LineAction:
    def __init__(self, line: Line, color, width) -> None:
        self.lines = [line]
        self.color = color
        self.width = width

    def add(self, velocity, angle) -> None:
        # start a new line
        last = self.lines[-1]
        x,y = last.end()
        self.lines.append(Line(x, y, velocity, angle))


    def update(self, screen, width, height):
        for line in self.lines:
            if not line.stopped:
                line.update(width, height)
                
            line.draw(screen, self.color)
            
    def stop(self):
        for line in self.lines:
            line.stop()


class SplatterAction:
    def __init__(self, splatter:Splatter) -> None:
        self.splatters = [splatter]
        
    def add(self, splatter):
        self.splatters.append(splatter)
        
    def update(self, screen):
        for splatter in self.splatters:
            splatter.draw(screen)