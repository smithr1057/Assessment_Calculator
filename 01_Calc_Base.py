# Functions
# Lets you change color of printed text easily
def color_text(text, color):
    # Code was found using chatGpt using prompt
    # "Python function that allows me to change the text color"
    # Code was changed a bit as some parts were unneeded

    # list of colors
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    # Prints text in specified color
    print(f"{colors[color]}{text}\033[0m")


# checks user answers with valid answer
def string_checker(question, num_letters, valid_list, custom_error=None):

    if custom_error is None:
        error = f"Please choose {valid_list[0]} or {valid_list[1]}"
    else:
        error = custom_error

    while True:

        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned
        if num_letters == 0:
            for i in valid_list:
                if response == i:
                    return i
        else:
            for i in valid_list:
                if response == i[:num_letters] or response == i:
                    return i

        # output error if item not in list
        print(error)
        print()


# Displays instructions
def instructions():
    return "*** Instructions ***"


# Main Routine
# Lists
yn_list = ['yes', 'no']
dimension_list = ['2d', '3d']
shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes']
shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone',
             'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes']

# Asks user if they want to read instructions, if yes output instructions
show_instructions = string_checker("Do you want to read the instructions? ", 1, yn_list)

if show_instructions == 'yes':
    instructions()

# Loop code until user quits
while True:
    # Ask user to pick 2d / 3d
    dimension = string_checker('2D or 3D shape? ', 1, dimension_list)

    if dimension == '2d':
        shape = string_checker("Enter the shape you want (or 'shapes' to see valid options): ", 0, shapes_2d,
                               "Please enter a valid shape, or enter 'shapes' to see the valid options. ")
        if shape == 'shapes':
            print("*** Valid 2D Shapes ***")
            print("Circle, Square, Rectangle, Triangle")
        elif shape == 'circle':
            pass

