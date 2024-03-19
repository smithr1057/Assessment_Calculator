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

    shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes']
    shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone',
                 'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes']

    while True:

        shape_list = shapes_2d if var_dimension == '2d' else shapes_3d

        shape = string_checker(f"Enter the shape you want (or 'shapes' to see valid options): ", 0,
                               shape_list,
                               f"Please enter a valid shape, or enter 'shapes' to see the valid options. ")

        if shape == 'shapes':
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

    if user_choice == 'cuboid':
        length = num_check('Length: ', 0)
        width = num_check('Width: ', 0)
        height = num_check('Height: ', 0)
        volume = length * width * height
        face_area = 2 * (length * width + width * height + length * height)

    elif user_choice == 'cylinder':
        radius = num_check('Radius: ', 0)
        length = num_check('Length: ', 0)
        volume = pi * radius ** 2 * length
        face_area = pi * radius * (radius + (length ** 2 + radius ** 2) ** 0.5)

    elif user_choice == 'triangular prism':
        base = num_check('Base (bottom side of the triangle): ', 0)
        height = num_check('Height: ', 0)
        length = num_check('Length: ', 0)
        if vol_face == 'surface area' or vol_face == 'both':
            s1 = num_check('Length of one of the triangle sides: ', 0)
            s2 = num_check('Length of one of the triangle sides: ', 0)
            s3 = num_check('Length of one of the triangle sides: ', 0)
            face_area = (s1 + s2 + s3) * length + base * height
        volume = 0.5 * base * height * length

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
        base = num_check('Base edge: ', 0)
        height = num_check('Height: ', 0)

        volume = base ** 2 * height / 3
        face_area = base ** 2 + 2 * base * (base ** 2 / 4 + height ** 2) ** 0.5

    else:
        if vol_face == 'volume':
            height = num_check('Height: ', 0)
            base_width = num_check('Height: ', 0)
            base_height = num_check('Height: ', 0)
            base_area = 0.5 * base_width * base_height
            volume = 1 / 3 * base_area * height

        else:
            s1 = num_check('Length of one of the triangle sides: ', 0)
            s2 = num_check('Length of one of the triangle sides: ', 0)
            s3 = num_check('Length of one of the triangle sides: ', 0)
            slant_height = num_check('Height: ', 0)

            base_perimeter = s1 + s2 + s3
            s = base_perimeter / 2
            base_area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

            if vol_face == 'both':
                height = num_check('Height: ', 0)
                volume = 1 / 3 * base_area * height

            face_area = base_area + 1 / 2 * (base_perimeter * slant_height)

    print()

    if vol_face == 'volume':
        print(f'Volume: {volume:.2f}')

    elif vol_face == 'surface area':
        print(f'Surface Area: {face_area:.2f}')

    else:
        print(f'Volume: {volume:.2f}')
        print(f'Surface Area: {face_area:.2f}')
    print()
