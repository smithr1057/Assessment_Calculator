# V2 - simpler way to do a random color

import random

# Your text
text = "Hello, world!"

# List of ANSI escape codes for colors
colors = [
    '\033[31m',  # Red
    '\033[33m',  # Yellow
    '\033[32m',  # Green
    '\033[36m',  # Cyan
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
]

# Choose a random color
color = random.choice(colors)
# Print the character in the chosen color
print(color + text)
