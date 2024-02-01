import pygame

class Splatter:
    ## TODO
    def __init__(self, sprite_image, x, y, color, scale):
        self.sprite_image = pygame.transform.scale(sprite_image, (int(sprite_image.get_width() * scale), int(sprite_image.get_height() * scale)))
        self.x = x
        self.y = y
        self.color = color
        self.stopped = False
        
    def draw(self, screen):
        screen.blit(self.sprite_image, (self.x, self.y))