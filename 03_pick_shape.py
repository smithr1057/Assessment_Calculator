import math


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
        color_text(error, 'red')
        print()


# checks users enter a float between a low and high number
def num_check(question, low=None, high=None):
    # Used ChatGPT to allow the use of the letter 'x' used the prompt bellow
    # Make that function allow the letter 'x' to be used

    situation = ''
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:
            # Ask the question
            response = input(question)

            # Check if response is 'xxx'
            if response.lower() == 'xxx':
                return response

            # Convert the response to a float
            response = float(response)

            # Checks input is not too high or
            # too low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    color_text(f"Please enter a number between {low} and {high}", 'red')
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response <= low:
                    color_text(f"Please enter a number that is more than {low}", 'red')
                    continue

            return response

        except ValueError:
            color_text("Please enter a number", 'red')
            continue


# Main Routine
# Lists
dimension_list = ['2d', '3d']
shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes']
shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone',
             'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes']
area_perm_list = ['area', 'perimeter']
vol_face_list = ['volume', 'surface area']

# Set pi value
pi = math.pi

# Loop code until user quits
while True:
    # Ask user to pick 2d / 3d
    dimension = string_checker('2D or 3D shape? ', 1, dimension_list)

    if dimension == '2d':
        shape = string_checker("Enter the shape you want (or 'shapes' to see valid options): ", 0, shapes_2d,
                               "Please enter a valid shape, or enter 'shapes' to see the valid options. ")

        area_perm = string_checker("Do you want area, perimeter or both calculated? ", 1, area_perm_list)

        if shape == 'shapes':
            print("*** Valid 2D Shapes ***")
            print("Circle, Square, Rectangle, Triangle")

        elif shape == 'circle':
            print("you picked circle")

        elif shape == 'square':
            print("you picked square")

        elif shape == 'rectangle':
            print("you picked rectangle")

        else:
            print("you picked triangle")

    else:
        shape = string_checker("Enter the shape you want (or 'shapes' to see valid options): ", 0, shapes_2d,
                               "Please enter a valid shape, or enter 'shapes' to see the valid options. ")
        vol_face = string_checker('Do you want the volume, surface area or both calculated? ', 1, vol_face_list)

        if shape == 'shapes':
            print("*** Valid 3D Shapes ***")
            print("cuboid, cylinder, triangular prism, cone, sphere, "
                  "square based pyramid, triangle based pyramid, shapes")

        elif shape == 'cuboid':
            print("you picked cuboid")

        elif shape == 'cylinder':
            print("you picked cylinder")

        elif shape == 'triangular prism':
            print("you picked triangular prism")

        elif shape == 'cone':
            print("you picked cone")

        elif shape == 'sphere':
            print("you picked sphere")

        elif shape == 'square based pyramid':
            print("you picked square based pyramid")

        elif shape == 'triangle based pyramid':
            print("you picked triangle based pyramid")
