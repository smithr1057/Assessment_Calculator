import pandas
import math


# Functions
# Function to check numerical input
def num_check(question, low=None, high=None):
    while True:
        response = input(question)
        if response.lower() == 'xxx':
            return response
        try:
            num = float(response)
            if low is not None and num < low:
                raise ValueError(f"Please enter a number greater than or equal to {low}")
            if high is not None and num > high:
                raise ValueError(f"Please enter a number less than or equal to {high}")
            return num
        except ValueError as e:
            color_text(str(e), 'red')


# Prints out the valid shapes from the necessary list
def print_valid_shapes(dim, list_of_shapes):
    print()
    print(f"*** Valid {dim} Shapes ***")
    print(", ".join(list_of_shapes[:-2]))  # Exclude 'shapes' and 'xxx'
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


# Calculates shapes area and perimeter /
# volume and surface area and prints out the answer
def calc_shape(shape, dimension, to_calculate):

    # Set answer values
    answer_one = answer_two = ''

    # Set up the parameter dictionary
    parameter_dict = {}

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
            'cuboid': {'length': ('length', 'Length: ', '')},
            'cylinder': {'radius': ('radius', 'Radius: ', ''),
                         'height': ('height', 'Height: ', '')},

            'triangular prism': {
                'side1': ('side1', 'Enter the length of one of the triangles sides: ', ''),
                'side2': ('side2', 'Enter the length of a different side: ', ''),
                'side3': ('side3', 'Enter the length of the last side: ', ''),
                'length': ('length', 'Length: ', '')},

            'cone': {
                'radius': ('radius', 'Radius: ', ''),
                'height': ('height', 'Height: ', '')},

            'sphere': {'radius': ('radius', 'Radius: ', '')},

            'square based pyramid': {
                'width': ('width', 'Width: ', ''),
                'height': ('height', 'Height: ', '')},

            'triangle based pyramid': {
                'height': ('height', 'Height: ', ''),
                'base_area': ('base_area', 'Area of base triangle: ', ''),
                'base_edge': ('base_edge', 'Base of one of the faces: ', '')
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
                'volume': lambda a, h: 1/3 * a * h,
                'surface area': lambda b, a, h: a + (3/2) * b * h
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

    # Set the previously added parameters that aren't used for this shape to N/A
    for parameter, value_list in parameter_list_dict.items():
        if parameter not in inputs:
            value_list.append('N/A')

    # Iterate through parameters and values in inputs
    for key, value in inputs.items():
        # Add values into the corresponding list using the parameter_list_dict
        parameter_list_dict[key].append(value)
        # Add the parameter and list into parameter dictionary
        parameter_dict.update({key: parameter_list_dict[key]})

    # Add parameters of the shape and their values to the panda_dict
    panda_dict.update(parameter_dict)

    # If user wants 'area' / 'volume' or 'both' calculated
    if to_calculate == to_calculate_list[0] or to_calculate_list[2]:
        # Calculate area / volume based on the chosen shape and user inputs
        answer_one = shape_calculations[shape][to_calculate_list[0]](*inputs.values())

    # If user wants 'perimeter' / 'surface area' or 'both' calculated
    if to_calculate == to_calculate_list[1] or to_calculate_list[2]:
        # Calculate perimeter / surface area based on the chosen shape and user inputs
        answer_two = shape_calculations[shape][to_calculate_list[1]](*inputs.values())

    print()

    # If user asked for area / volume or both then print answer one (area / volume)
    if to_calculate == to_calculate_list[0] or to_calculate_list[2]:
        print(f'{to_calculate_list[0]}: {answer_one:.2f}')

    # If user asked for perimeter / surface area or both then print answer two (perimeter / surface area)
    if to_calculate == to_calculate_list[1] or to_calculate_list[2]:
        print(f'{to_calculate_list[1]}: {answer_two:.2f}')

    # If a 2d shape then add answer to the 2d shape lists
    if dimension == '2d':
        area_list.append(answer_one)
        perimeter_list.append(answer_two)
    # If a 3d shape then add answer to the 3d shape lists
    else:
        volume_list.append(answer_one)
        surface_area_list.append(answer_two)

    print()


# Main Routine
# Set pi
pi = math.pi


# Set up lists
yn_list = ['yes', 'no']
dimension_list = ['2d', '3d']
option_list_2d = ['area', 'perimeter', 'both']
option_list_3d = ['volume', 'surface area', 'both']

# Create empty lists for parameters
length_list = []
radius_list = []
width_list = []
side1_list = []
side2_list = []
side3_list = []

parameter_list_dict = {
    'length': length_list,
    'radius': radius_list,
    'width': width_list,
    'side1': side1_list,
    'side2': side2_list,
    'side3': side3_list
}

while True:
    # Set up lists for answers
    # 2d answers
    area_list = []
    perimeter_list = []
    answer_2d_dict = {
        'Area': area_list,
        'perimeter': perimeter_list
    }

    # 3d answers
    volume_list = []
    surface_area_list = []
    answer_3d_dict = {
        'Volume': volume_list,
        'surface area': surface_area_list
    }

    # Create empty lists for parameters
    length_list = []
    radius_list = []
    width_list = []
    side1_list = []
    side2_list = []
    side3_list = []

    # Create dict to link parameters to their lists
    parameter_list_dict = {
        'length': length_list,
        'radius': radius_list,
        'width': width_list,
        'side1': side1_list,
        'side2': side2_list,
        'side3': side3_list
    }

    # Set up a list for shapes
    shape_list = []

    # Create the dict used for the panda
    panda_dict = {
        "Shape": shape_list
    }

    # Ask user to choose between 2d or 3d shapes
    dimensions = string_checker("2D or 3D shape? ", 1, dimension_list)
    print()

    while True:
        # Asks user for a valid shape as per earlier choice
        user_shape = get_user_input(dimensions)

        # If user enters 'xxx' quit
        if user_shape == 'xxx':
            break

        # Add shape to shape_list for panda
        shape_list.append(user_shape)

        print()

        # Ask if user wants area or perimeter calculated
        if dimensions == '2d':
            whats_calculated = string_checker("Do you want area, perimeter or both calculated? ", 1, option_list_2d)
        # Ask if user wants volume or surface area calculated
        else:
            whats_calculated = string_checker('Do you want the volume, surface area or both calculated? ', 1,
                                              option_list_3d)

        # Use calc shape func to calculate answer,
        calc_shape(user_shape, dimensions, whats_calculated)

    # Add the answers to the panda dictionary
    # If 2d add the 2d answers
    if dimensions == '2d':
        panda_dict.update(answer_2d_dict)
    # If 3d add the 3d answers
    else:
        panda_dict.update(answer_3d_dict)

    # Print the dictionary used for pandas for testing
    print(panda_dict)

    # Create the table frame for our data
    results_frame = pandas.DataFrame(panda_dict)

    # set index
    results_frame = results_frame.set_index('Shape')

    # Print the panda
    print(results_frame)

    # Ask user if they want to use the calculator again
    use_again = string_checker('Would you like to go again? ', 1, yn_list)
    # If not then exit the calculator
    if use_again == 'no':
        break

print('Bye Bye')
