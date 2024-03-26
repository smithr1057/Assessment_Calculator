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


# Prints out the valid shapes from the necessary list
def print_valid_shapes(dim, shape_list):
    print(f"*** Valid {dim} Shapes ***")
    print(", ".join(shape_list))


# Asks user for the shape they want and returns it
def get_user_input(var_dimension):

    # set up valid shape lists including the word 'shapes'
    shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes']
    shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone',
                 'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes']

    while True:
        # pick the valid shape list for 2d or 3d
        shape_list = shapes_2d if var_dimension == '2d' else shapes_3d

        # Ask user for shape if it's not valid then output custom error
        shape = string_checker(f"Enter the shape you want (or 'shapes' to see valid options): ", 0,
                               shape_list,
                               f"Please enter a valid shape, or enter 'shapes' to see the valid options. ")

        if shape == 'shapes':
            # Print out the valid shapes using function
            print_valid_shapes(var_dimension, shapes_2d if var_dimension == '2d' else shapes_3d)
        else:
            return shape


# Main Routine
# Lists
vol_face_list = ['volume', 'surface area', 'both']

# Set pi value
pi = math.pi

# Loop code until user quits
while True:

    volume = 0
    face_area = 0

    user_choice = get_user_input('3d')
    vol_face = string_checker('Do you want the volume, surface area or both calculated? ', 1, vol_face_list)

    # Ask user for required information Then calculate volume / surface area
    if user_choice == 'cuboid':
        length = num_check('Edge Length: ', 0)
        volume = length ** 3
        face_area = 2 * (length * length + length * length + length * length)

    elif user_choice == 'cylinder':
        radius = num_check('Radius: ', 0)
        height = num_check('Height: ', 0)
        volume = pi * radius ** 2 * height
        face_area = 2 * pi * radius * height + 2 * pi * radius ** 2

    elif user_choice == 'triangular prism':
        a = num_check('Length of one side of the triangle: ', 0)
        b = num_check('Length of another side of the triangle: ', 0)
        c = num_check('Length of the last side of the triangle: ', 0)
        length = num_check('Length: ', 0)

        lat_area = length * (a + b + c)
        bot_area = 1 / 4 * ((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)) ** 0.5

        volume = 1 / 4 * length * ((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)) ** 0.5
        face_area = lat_area + bot_area + bot_area

    elif user_choice == 'cone':
        radius = num_check('Radius: ', 0)
        height = num_check('Height: ', 0)

        volume = 1/3 * pi * radius ** 2 * height
        face_area = pi * radius * (radius + (height ** 2 + radius ** 2) ** 0.5)

    elif user_choice == 'sphere':
        radius = num_check('Radius: ', 0)

        volume = 4 / 3 * pi * radius ** 3
        face_area = 4 * pi * radius ** 2

    elif user_choice == 'square based pyramid':
        width = num_check('Width: ', 0)
        height = num_check('Height: ', 0)

        volume = width ** 2 * height / 3
        face_area = width ** 2 + 2 * width * (width ** 2 / 4 + height ** 2) ** 0.5

    else:

        height = num_check('Height: ', 0)
        base_width = num_check('Width of the base triangle: ', 0)
        apothem = num_check('Apothem length: ', 0)

        base_area = 0.5 * apothem * base_width
        volume = (1 / 6) * base_area * height

        if vol_face == 'both' or vol_face == 'surface area':
            sl_height = num_check('Slant_height: ', 0)
            face_area = base_area + ((3 / 2) * sl_height)
            
    print()

    if vol_face == 'volume':
        print(f'Volume: {volume:.2f}')

    elif vol_face == 'surface area':
        print(f'Surface Area: {face_area:.2f}')

    else:
        print(f'Volume: {volume:.2f}')
        print(f'Surface Area: {face_area:.2f}')
    print()
