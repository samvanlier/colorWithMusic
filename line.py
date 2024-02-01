import math
import pygame

class Line:
    def __init__(self, start_x, start_y, velocity, angle):
        self.start_x = start_x
        self.end_x = start_x
        self.start_y = start_y
        self.end_y = start_y
        self.velocity = velocity 
        # TODO make angle psuedo random?
        self.angle = math.radians(angle)
        self.stopped = False
        
    def update(self, width, height):
        """update the properties of the line
        
        If the line is `stopped`, the update is not executed anymore
        """
        if not self.stopped:
            # update the ending coordinates based on the initial velocity and angl
            delta_x = self.velocity * math.cos(self.angle)
            delta_y = self.velocity * math.sin(self.angle)
            self.end_x = self.end_x + delta_x
            self.end_y = self.end_y + delta_y
            
            if self.end_x > width  or self.end_y > height:
                self.stopped = True
                # let line go to edge, not cross it
                self.end_x = min(self.end_x, width)
                self.end_y = min(self.end_y, height)
            if self.end_x < 0 or self.end_y < 0:
                self.stopped = True
                self.end_x = max(0, self.end_x)
                self.end_y = max(0, self.end_y)
                
    def draw(self, screen, color):
        start = (self.start_x, self.start_y)
        end = (self.end_x, self.end_y)
        pygame.draw.line(screen, color, start, end, int(self.velocity))
    
    def stop(self):
        self.stopped = True
        
    def start(self):
        return (self.start_x, self.start_y)
    
    def end(self):
        return (self.end_x, self.end_y)