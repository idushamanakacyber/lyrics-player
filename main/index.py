import pygame
import time
import sys
import threading
import os

# ANSI color codes for beautiful colour changes
colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]

reset = "\033[0m"

# Lyrics with start times and durations in seconds
lyrics_with_times = [
    (47, "සන්තාන සුසුම් දවටා", 5),
    (53, "හන්තාන සුළඟ හැමුවා", 5),
    (58, "මං ගාව රැළිති නගවා", 5),
    (64, "ගංගාව ඔහේ ගැලුවා", 4),
    (69, "ගංගාව ඔහේ ගැලුවා", 5),
    (97, "මල් වීදී අතර සඟවා", 5),
    (103, "ගිය හාදු ඇතිද බැලුවා", 4),
    (108, "වැල් පාලම ගත සොලවා", 5),
    (114, "අපි බයද කියා බැලුවා", 4),
    (123, "සන්තාන සුසුම් දවටා", 4),
    (128, "හන්තාන සුළඟ හැමුවා", 5),
    (133, "මං ගාව රැළිති නගවා", 5),
    (139, "ගංගාව ඔහේ ගැලුවා", 6),
    (145, "ගංගාව ඔහේ ගැලුවා", 5),
    (173, "වැදි රජුට කඩුව පවරා", 4),
    (178, "වල ළඟදි මනමේ හැඬුවා", 5),
    (184, "ඒ මතක සියලු සඟවා", 5),
    (190, "මහවැලිය ඔහේ ගැලුවා", 4),
    (198, "සන්තාන සුසුම් දවටා", 5),
    (204, "හන්තාන සුළඟ හැමුවා", 4),
    (209, "මං ගාව රැළිති නගවා", 4),
    (214, "ගංගාව ඔහේ ගැලුවා", 5),
    (220, "ගංගාව ඔහේ ගැලුවා", 4),
    (225, "ගංගාව ඔහේ ගැලුවා", 12),
]

# Function to type the lyrics in sync
def type_lyrics():
    audio_start = time.time()
    previous_end = 0
    color_index = 0
    for start_time, line, duration in lyrics_with_times:
        printed_dots = False
        last_dot_time = time.time()
        while time.time() - audio_start < start_time:
            time.sleep(0.01)
            if time.time() - last_dot_time >= 1:
                sys.stdout.write('.')
                sys.stdout.flush()
                last_dot_time = time.time()
                printed_dots = True
        if printed_dots:
            sys.stdout.write('\n')
            sys.stdout.flush()
        
        letter_delay = duration / len(line) if len(line) > 0 else 0.1
        
        # Get colour for this line
        color = colors[color_index % len(colors)]
        color_index += 1
        
        # Print letter by letter
        sys.stdout.write(color)
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(letter_delay)
        sys.stdout.write(reset + "\n")
        sys.stdout.flush()
        
        previous_end = start_time + duration

pygame.mixer.init()
pygame.mixer.music.load("santhana_susum.mp3")  
pygame.mixer.music.play()

lyrics_thread = threading.Thread(target=type_lyrics)
lyrics_thread.start()

while pygame.mixer.music.get_busy():
    time.sleep(1)

lyrics_thread.join()

print("Song finished! - by Idusha Manaka")
