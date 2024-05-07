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
    return f"{colors[color]}{text}\033[0m"


# checks user answers with valid answer
def string_checker(question, num_letters, valid_list, custom_error=None):

    if custom_error is None:
        if len(valid_list) == 3:
            error = f"Please choose {valid_list[0]}, {valid_list[1]} or {valid_list[2]}"
        else:
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
        print(color_text(error, 'red'))
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


# Displays instructions
def instructions():
    return "*** Instructions ***"


# Prints out the valid shapes from the necessary list
def print_valid_shapes(dim, shape_list):
    print()
    print(f"*** Valid {dim} Shapes ***")
    print(", ".join(shape_list[:-1]))  # Exclude 'shapes'
    print()


# Asks user for the shape they want and returns it
def get_user_input(var_dimension):

    # set up valid shape lists including the word 'shapes'
    shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes', 'xxx']
    shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone',
                 'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes', 'xxx']

    while True:
        # pick the valid shape list for 2d or 3d
        shape_list = shapes_2d if var_dimension == '2d' else shapes_3d

        # Ask user for shape if it's not valid then output custom error
        shape = string_checker(f"Enter the shape you want ('shapes' to see valid options / 'xxx' to quit): ", 0,
                               shape_list,
                               f"Please enter a valid shape, or enter 'shapes' to see the valid options / "
                               f"'xxx' to quit. ")

        if shape == 'shapes':
            # Print out the valid shapes using function
            print_valid_shapes(var_dimension, shapes_2d if var_dimension == '2d' else shapes_3d)
        else:
            return shape


# Calculates shapes area and perimeter /
# volume and surface area and prints out the answer
def calc_shape(shape, dimension, to_calculate):

    # Set answer values
    answer_one = answer_two = ''

    # Set input prompts and shape calculations
    if dimension == '2d':

        to_calculate_list = ['area', 'perimeter', 'both']

        # Dictionary containing prompts and units for each input
        input_prompts = {
            'circle': {'radius': ('radius', 'Enter radius of the circle (half the diameter): ', '')},
            'square': {'length': ('length', 'Enter length of the square: ', '')},
            'rectangle': {'length': ('length', 'Enter length of the rectangle: ', ''),
                          'width': ('width', 'Enter width of the rectangle: ', '')},
            'triangle': {'side1': ('side1', 'Enter the length of one of the sides: ', ''),
                         'side2': ('side2', 'Enter the length of a different side: ', ''),
                         'side3': ('side3', 'Enter the length of the last side: ', '')}
        }

        # Dictionary containing formulas for area and perimeter calculation for each shape
        shape_calculations = {
            'circle': {
                'area': lambda r: pi * r ** 2,
                'perimeter': lambda r: 2 * pi * r
            },
            'square': {
                'area': lambda s: s ** 2,
                'perimeter': lambda s: 4 * s
            },
            'rectangle': {
                'area': lambda l, w: l * w,
                'perimeter': lambda l, w: 2 * (l + w)
            },
            'triangle': {
                'area': lambda s1, s2, s3: (((s1 + s2 + s3) / 2) *
                                            (((s1 + s2 + s3) / 2) - s1) *
                                            (((s1 + s2 + s3) / 2) - s2) *
                                            (((s1 + s2 + s3) / 2) - s3)) ** 0.5,
                'perimeter': lambda s1, s2, s3: s1 + s2 + s3
            }
        }
    else:

        to_calculate_list = ['volume', 'surface area', 'both']

        # Dictionary mapping shapes to their parameters and prompts
        input_prompts = {
            'cuboid': {
                'length': ('length', 'Length: ', '')
            },

            'cylinder': {
                'radius': ('radius', 'Radius: ', ''),
                'height': ('height', 'Height: ', '')
            },
            'triangular prism': {
                'side1': ('side1', 'Enter the length of one of the triangles sides: ', ''),
                'side2': ('side2', 'Enter the length of a different side: ', ''),
                'side3': ('side3', 'Enter the length of the last side: ', ''),
                'length': ('length', 'Length: ', '')
            },

            'cone': {
                'radius': ('radius', 'Radius: ', ''),
                'height': ('height', 'Height: ', '')
            },

            'sphere': {
                'radius': ('radius', 'Radius: ', '')
            },

            'square based pyramid': {
                'width': ('width', 'Width: ', ''),
                'height': ('height', 'Height: ', '')
            },

            'triangle based pyramid': {
                'height': ('height', 'Height: ', ''),
                'base_width': ('width', 'Width of the base triangle: ', ''),
                'apothem': ('apothem', 'Apothem length: ', ''),
                'sl_height': ('slant', 'Slant_height: ', '')
            }
        }

        # Dictionary mapping shapes to their formulas for volume and surface area
        shape_calculations = {
            'cuboid': {
                'volume': lambda l: l ** 3,
                'surface area': lambda l: 2 * (l * l + l * l + l * l)
            },
            'cylinder': {
                'volume': lambda r, h: pi * r ** 2 * h,
                'surface area': lambda r, h: 2 * pi * r * h + 2 * pi * r ** 2
            },
            'triangular prism': {
                'volume': lambda a, b, c, l: 1 / 4 * l * ((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)) ** 0.5,
                'surface area': lambda a, b, c, l: l * (a + b + c) + 1 / 4 * (
                            (a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)) ** 0.5 + 1 / 4 * (
                                                               (a + b + c) * (b + c - a) * (c + a - b) * (
                                                                   a + b - c)) ** 0.5
            },
            'cone': {
                'volume': lambda r, h: 1 / 3 * pi * r ** 2 * h,
                'surface area': lambda r, h: pi * r * (r + (h ** 2 + r ** 2) ** 0.5)
            },
            'sphere': {
                'volume': lambda r: 4 / 3 * pi * r ** 3,
                'surface area': lambda r: 4 * pi * r ** 2
            },
            'square based pyramid': {
                'volume': lambda w, h: w ** 2 * h / 3,
                'surface area': lambda w, h: w ** 2 + 2 * w * (w ** 2 / 4 + h ** 2) ** 0.5
            },
            'triangle based pyramid': {
                'volume': lambda bw, a, h: (1 / 6) * (0.5 * bw * a) * h,
                'surface area': lambda bw, a, h, sl: (0.5 * bw * sl) + ((3 / 2) * sl)
            }
        }

    # Retrieve prompts for user inputs associated with the chosen shape
    prompts = input_prompts[shape]

    # Create dictionary for user inputs needed for calculation
    inputs = {
        # Get user input for each parameter then iterate over parameter and prompt
        key: num_check(prompt[1], 0)
        for key, prompt in prompts.items()
    }

    if to_calculate == to_calculate_list[0] or to_calculate_list[2]:
        # Calculate area based on the chosen shape and user inputs
        answer_one = shape_calculations[shape][to_calculate_list[0]](*inputs.values())

    if to_calculate == to_calculate_list[1] or to_calculate_list[2]:
        # Calculate perimeter based on the chosen shape and user inputs
        answer_two = shape_calculations[shape][to_calculate_list[1]](*inputs.values())

    print()
    if to_calculate == to_calculate_list[0] or to_calculate_list[2]:
        print(f'{to_calculate_list[0]}: {answer_one:.2f}')

    if to_calculate == to_calculate_list[1] or to_calculate_list[2]:
        print(f'{to_calculate_list[1]}: {answer_two:.2f}')
    print()


# Main Routine

# Set pi value
pi = math.pi

# Lists
yn_list = ['yes', 'no']
dimension_list = ['2d', '3d']
area_perm_list = ['area', 'perimeter', 'both']
vol_face_list = ['volume', 'surface area', 'both']


# Dictionaries

# Asks user if they want to read instructions, if yes output instructions
show_instructions = string_checker("Do you want to read the instructions? ", 1, yn_list)

if show_instructions == 'yes':
    instructions()

# Loop code until user quits
while True:
    # Ask user to choose between 2d or 3d shapes
    dimensions = string_checker("2D or 3D shape? ", 1, dimension_list)

    # Asks user for a valid shape as per earlier choice
    user_shape = get_user_input(dimensions)

    if user_shape == 'xxx':
        break

    print()

    if dimensions == '2d':
        whats_calculated = string_checker("Do you want area, perimeter or both calculated? ", 1, area_perm_list)
    else:
        whats_calculated = string_checker('Do you want the volume, surface area or both calculated? ', 1, vol_face_list)

    answers = calc_shape(user_shape, dimensions, whats_calculated)

print(color_text('Thank you for using the Super Shape Calculator', 'green'))
