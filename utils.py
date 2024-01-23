colors = {
    "A": [10, 210, 255],
    "B": [41, 98, 255],
    "C": [149, 0, 255],
    "D": [255, 0, 89],
    "E": [255, 140, 0],
    "F": [180, 230, 0],
    "G": [15, 255, 219]
} 


def midi_note_to_name(note_number):
    """convert a midi note number to the note name

    Args:
        note_number (int): the midi number

    Returns:
        string: the name of the note
    """
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = note_number // 12 - 1
    note_name = notes[note_number % 12]
    return note_name, octave

def generate_color(note_number, velocity):
    """create a and RGBA tuple for the given midi note and velocity. The note will indicate the color and the velocity will influence the alpha value.

    Args:
        note_number (int): the midi note number
        velocity (int): the velocity of the played note
    Returns:
        int, int, int, int: a tuple representing a RGBA color.
    """
    color = note_as_color(note_number)
    alpha = velocity_as_alpha(velocity)
    rgba = []
    for c in color:
        rgba.append(c)
    # rgba.append(alpha)
    return tuple(rgba)

def note_as_color(note_number):
    note, _ = midi_note_to_name(note_number)
    return colors[note.replace('#', '')]

def velocity_as_alpha(velocity):
    # scale value between 0 and 255
    velocity =  max(0, min(127, velocity))
    
    # Scale the MIDI velocity to the range 0-255
    return int((velocity / 127) * 255)