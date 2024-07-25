'''
Pip Install Playsound  in the terminal
Basically the module helps us to play sound.


Search on Internet playsound to copy the commands:

 from playsound import playsound
 playsound('/path/to/a/sound/file/you/want/to/play.mp3')

from here: https://pypi.org/project/playsound/

'''

# the above didn't worked, so usedthe below by doing this : pip install pygame

import pygame  # Import the pygame library

# Initialize the mixer module to handle audio
pygame.mixer.init()

# Load the MP3 audio file into the mixer
pygame.mixer.music.load(r'E:\#PYTHON\PYTHON\Chapter_1\sage_ritviz.mp3')

# Play the loaded audio file
pygame.mixer.music.play()

# Keep the program running while the audio is playing
while pygame.mixer.music.get_busy():  # Check if the audio is still playing
    pygame.time.Clock().tick(10)  # Wait for a short period to reduce CPU usage


# from playsound import playsound
# playsound('E:\\#PYTHON\\PYTHON\\Chapter_1\\sage_ritviz.mp3')

# Copied the mp3 file path from file manager and copied here.

# Now, Important: Whenever we write path for windows:
# We should write double back-slash.
# Because when we write a character after single back-slash
# it is considered as an escape sequence character.