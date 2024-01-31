import pygame
import sys
import mido
import random
from utils import *
from action import LineAction
from line import Line
import logging

class NoteAction: 
    def __init__(self, velocity, color):
        self.updated = False
        self.velocity = velocity
        self.color = color
        
    def update(self, velocity, color):
        self.updated = True
        self.velocity = velocity
        self.color = color

    def stopped(self):
        return self.velocity == 0


# Initialize Pygame
pygame.init()

# Configure the logging system
logging.basicConfig(level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

# Set up display
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Real-time Line Drawing")
surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Store actions
notes = {}

# lines dict: {noteName: Action}
lines = {}
splatter = {}

def update():
    if len(notes) < 0:
        return None
    
    for note, action in notes.items():
        if '#' not in note:
            # note is a line
            if note not in lines:
                # first time played
                # TODO set x, y and angle random
                # TODO implement color stuff
                lines[note] = LineAction(
                    Line(random.randint(0, width), random.randint(0, height), action.velocity/10, random.randint(0, 360)), 
                    action.color,
                    action.velocity % 15)
            else:
                # note is already played
                if action.stopped():
                    # stop drawing the line
                    lines[note].stop()
                    action.updated = False
                else:
                    if action.updated:
                        # note is played again or the velocity changed (new line)
                        # TODO angle selection bit les random
                        lines[note].add(action.velocity, random.randint(0, 360))
                        action.updated = False
        else:
            # note is a splatter
            if note not in splatter:
                pass

def draw_lines():
    for _, action in lines.items():
        action.update(screen, width, height)

def update_action(note_number, velocity):
    color = generate_color(note_number, velocity)
    note, _ = midi_note_to_name(note_number)
    velocity = int(velocity / 5)
    # print(f"name: {note}, velocity: {velocity}")
    
    if note in notes:
        # update note
        notes[note].update(velocity, color)
    else:
        # create action
        notes[note] = NoteAction(velocity, color)

# setup music tools
def on_midi_message(message):
    if message.type == 'note_on':
        update_action(message.note, message.velocity)

keyboard_name = "Impact GX Mini MIDI1"
input_port = mido.open_input(keyboard_name, callback=on_midi_message)

# Main game loop
running = True
random.seed(1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)
        
    update()
    if len(lines) > 0:
        draw_lines()
        
    # screen.blit(surface, (0,0))
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
input_port.close()
pygame.quit()
sys.exit()
