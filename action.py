from line import Line
import logging

logger = logging.getLogger(__name__)

class Action:
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
                
            line.draw(screen, self.color, self.width)
            
    def stop(self):
        for line in self.lines:
            line.stop()
