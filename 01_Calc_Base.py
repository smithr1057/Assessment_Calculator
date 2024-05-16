import math
import pandas
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
    return ''


# Prints out the valid shapes from the necessary list
def print_valid_shapes(dim, list_of_shapes):
    print()
    print(color_text(f"*** Valid {dim} Shapes ***", 'blue'))
    print(", ".join(list_of_shapes[:-1]))  # Exclude 'shapes'
    print()


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
        shape = string_checker(f"Enter the shape you want ('shapes' to see valid options): ", 0,
                               shape_list,
                               f"Please enter a valid shape, or enter 'shapes' to see the valid options.")

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

    # Set up the parameter dictionary
    parameter_dict = {}

    # Set input prompts and shape calculations
    if dimension == '2d':

        dimension_parameter_lists = parameter_2d_list_dict

        to_calculate_list = ['area', 'perimeter', 'both']

        # Dictionary containing prompts and units for each input
        input_prompts = {
            'circle': {'radius': ('radius', 'Radius: ', '')},
            'square': {'length': ('length', 'Length: ', '')},
            'rectangle': {'length': ('length', 'Length: ', ''),
                          'width': ('width', 'Width: ', '')},
            'triangle': {'side1': ('side1', 'First side: ', ''),
                         'side2': ('side2', 'Second side: ', ''),
                         'side3': ('side3', 'Third side: ', '')}
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
                'area': lambda s1, s2, s3: (((s1 + s2 + s3) / 2) * (((s1 + s2 + s3) / 2) - s1) * (((s1 + s2 + s3) / 2) - s2) * (((s1 + s2 + s3) / 2) - s3)) ** 0.5,
                'perimeter': lambda s1, s2, s3: s1 + s2 + s3
            }
        }
    else:

        dimension_parameter_lists = parameter_3d_list_dict

        to_calculate_list = ['volume', 'surface area', 'both']

        # Dictionary mapping shapes to their parameters and prompts
        input_prompts = {
            'cuboid': {'length': ('length', 'Length: ', '')},
            'cylinder': {'radius': ('radius', 'Radius: ', ''),
                         'height': ('height', 'Height: ', '')},

            'triangular prism': {
                'side1': ('side1', 'First side of triangle: ', ''),
                'side2': ('side2', 'Second side of triangle: ', ''),
                'side3': ('side3', 'Third side of triangle: ', ''),
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
    for parameter, value_list in dimension_parameter_lists.items():
        if parameter not in inputs:
            value_list.append('N/A')

    # Iterate through parameters and values in inputs
    for key, value in inputs.items():
        # Add values into the corresponding list using the parameter_list_dict
        dimension_parameter_lists[key].append(value)
        # Add the parameter and list into parameter dictionary
        parameter_dict.update({key: dimension_parameter_lists[key]})

    # Add parameters of the shape and values to the corresponding panda_dict
    if dimension == '2d':
        panda_2d_dict.update(parameter_dict)
    else:
        panda_3d_dict.update(parameter_dict)

    # If user wants 'area' / 'volume' or 'both' calculated
    if to_calculate == to_calculate_list[0] or to_calculate_list[2]:
        # Calculate area / volume based on the chosen shape and user inputs
        answer_one = shape_calculations[shape][to_calculate_list[0]](*inputs.values())
        answer_one = round(answer_one, 2)

    # If user wants 'perimeter' / 'surface area' or 'both' calculated
    if to_calculate == to_calculate_list[1] or to_calculate_list[2]:
        # Calculate perimeter / surface area based on the chosen shape and user inputs
        answer_two = shape_calculations[shape][to_calculate_list[1]](*inputs.values())
        answer_two = round(answer_two, 2)

    print()

    # If user asked for area / volume or both then print answer one (area / volume)
    if to_calculate == to_calculate_list[0] or to_calculate_list[2]:
        print(f'{to_calculate_list[0]}: {answer_one}')

    # If user asked for perimeter / surface area or both then print answer two (perimeter / surface area)
    if to_calculate == to_calculate_list[1] or to_calculate_list[2]:
        print(f'{to_calculate_list[1]}: {answer_two}')

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
dimension_list = ['2d', '3d', 'xxx']
option_list_2d = ['area', 'perimeter', 'both']
option_list_3d = ['volume', 'surface area', 'both']


# Set up lists for answers
# 2d answers
area_list = []
perimeter_list = []
answer_2d_dict = {
    'Area': area_list,
    'Perimeter': perimeter_list
}

# 3d answers
volume_list = []
surface_area_list = []
answer_3d_dict = {
    'Volume': volume_list,
    'Surface Area': surface_area_list
}

# Create empty lists for 2d parameters
length_2d_list = []
radius_2d_list = []
width_2d_list = []
side1_2d_list = []
side2_2d_list = []
side3_2d_list = []

# Create dict to link 2d parameters to their lists
parameter_2d_list_dict = {
    'length': length_2d_list,
    'radius': radius_2d_list,
    'width': width_2d_list,
    'side1': side1_2d_list,
    'side2': side2_2d_list,
    'side3': side3_2d_list,

}

# Create empty lists for 3d parameters
length_3d_list = []
radius_3d_list = []
width_3d_list = []
height_3d_list = []
side1_3d_list = []
side2_3d_list = []
side3_3d_list = []
base_area_list = []
base_edge_list = []

# Create dict to link 3d parameters to their lists
parameter_3d_list_dict = {
    'length': length_3d_list,
    'radius': radius_3d_list,
    'width': width_3d_list,
    'height': height_3d_list,
    'side1': side1_3d_list,
    'side2': side2_3d_list,
    'side3': side3_3d_list,
    'base_area': base_area_list,
    'base_edge': base_edge_list
}

# Set up a list for 2d shapes
shape_2d_list = []

# Create the dict used for the 2d panda
panda_2d_dict = {
    "Shape": shape_2d_list
}

# Set up a list for 3d shapes
shape_3d_list = []

# Create the dict used for the 3d panda
panda_3d_dict = {
    "Shape": shape_3d_list
}

print(color_text("<<<<< Welcome to the Super Shape Calculator! >>>>>", 'blue'))
print("This program helps you calculate the area, perimeter, volume, and surface area of various shapes.")
print()

# Asks user if they want to read instructions, if yes output instructions
show_instructions = string_checker("Do you want to read the instructions? ", 1, yn_list)

if show_instructions == 'yes':
    instructions()

# Loop code until user quits
while True:

    # Ask user to choose between 2d or 3d shapes
    dimensions = string_checker("2D or 3D shape (or 'xxx' to quit)? ", 1, dimension_list)

    # If user enters 'xxx' quit
    if dimensions == 'xxx':
        break

    print()
    # Asks user for a valid shape as per earlier choice
    user_shape = get_user_input(dimensions)

    print()

    # Ask if user wants area or perimeter calculated
    if dimensions == '2d':
        # Add shape to shape_list for panda
        shape_2d_list.append(user_shape)

        whats_calculated = string_checker("Do you want area, perimeter or both calculated? ", 1, option_list_2d)
    # Ask if user wants volume or surface area calculated
    else:
        # Add shape to shape_list for panda
        shape_3d_list.append(user_shape)

        whats_calculated = string_checker('Do you want the volume, surface area or both calculated? ', 1,
                                          option_list_3d)

    # Use calc shape func to calculate answer,
    calc_shape(user_shape, dimensions, whats_calculated)

    # Add the answers to the panda dictionary
    # If 2d add the 2d answers
    if dimensions == '2d':
        panda_2d_dict.update(answer_2d_dict)

    # If 3d add the 3d answers
    else:
        panda_3d_dict.update(answer_3d_dict)

    # If there is a 2d shape then make and output panda
if len(shape_2d_list) > 0:

    print()
    print(color_text("**** 2D Shapes ****", 'blue'))

    # Create the table frame for our data
    results_2d_frame = pandas.DataFrame(panda_2d_dict)

    # set index
    results_2d_frame = results_2d_frame.set_index('Shape')

    # Print the panda
    print(results_2d_frame)

    # If there is a 3d shape then make and output panda
if len(shape_3d_list) > 0:

    print()
    print(color_text("**** 3D Shapes ****", 'blue'))

    # Create the table frame for our data
    results_3d_frame = pandas.DataFrame(panda_3d_dict)

    # set index
    results_3d_frame = results_3d_frame.set_index('Shape')

    # Print the panda
    print(results_3d_frame)

print()
print(color_text('Thank you for using the Super Shape Calculator', 'green'))
