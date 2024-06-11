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
def num_check(question, low=None):

    while True:
        try:
            # Ask the question
            response = input(question)

            # Check if response is 'xxx'
            if response.lower() == 'xxx':
                return response

            # Convert the response to a float
            response = float(response)

            # Checks input is not too low
            if response <= low:
                print(color_text(f"Please enter a number that is more than {low}", 'red'))
                continue

            return response

        except ValueError:
            print(color_text("Please enter a number", 'red'))
            continue


# Displays instructions
def instructions():
    print(color_text("***** Instructions *****", 'green'))
    print("""
This Super Shape Calculator helps you calculate various properties of 2D and 3D shapes.

Here's how to use it:

1. **Choose Shape**: 
   - When prompted, enter the shape you want to calculate properties for. 
   - Type 'shapes' to see the list of valid shape options or 'xxx' to quit the program.
   - The program will automatically determine whether your shape is 2D or 3D.

2. **Choose Calculation**:
   - For 2D shapes, you can choose to calculate the area, perimeter, or both.
   - For 3D shapes, you can choose to calculate the volume, surface area, or both.

3. **Enter Dimensions**:
   - The program will prompt you to enter the necessary dimensions for the chosen shape (e.g., radius for a circle, length and width for a rectangle).

4. **View Results**:
   - The program will display the calculated properties (area, perimeter, volume, or surface area) of the shape.
   - At the end of the session, the program will display a summary table of all shapes and their calculated properties.
   - You will also have the option to save the results to a file.

5. **Quit the Program**:
   - To exit the program, type 'xxx' when prompted for a shape.

Enjoy using the Super Shape Calculator!
""")


# Prints out the valid shapes from the necessary list
def print_valid_shapes(dim, list_of_shapes):
    print()
    print(color_text(f"*** Valid {dim} Shapes ***", 'blue'))
    if dim == '3D':
        print(", ".join(list_of_shapes) + ' (only regular tetrahedron)')
    else:
        print(", ".join(list_of_shapes))
    print()


# Asks user for the shape they want and returns it
def get_user_input():
    # valid shapes
    shape_list = ['circle', 'square', 'rectangle', 'triangle', 'cuboid', 'cube', 'cylinder', 'triangular prism',
                  'cone', 'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes']

    while True:

        # Ask user for shape if it's not valid then output custom error
        shape = string_checker(f"Enter a shape ('shapes' for valid options, 'xxx' to quit): ", 0,
                               shape_list + ['xxx'],
                               f"Please enter a valid shape, 'shapes' to see the valid options, or 'xxx' to quit.")

        if shape == 'shapes':
            # Print out the valid shapes using function
            print_valid_shapes('2D', shapes_2d)
            print_valid_shapes('3D', shapes_3d)

        else:
            return shape


def herons_formula(a, b, c):
    # Calculate area of triangle with heron's formula
    s = (a + b + c) / 2  # semi perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Calculates shapes area and perimeter /
# volume and surface area and prints out the answer
def calc_shape(shape, dimension, to_calculate):

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

        # Dictionary containing formulas for area and perimeter for each shape
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
                'area': lambda s1, s2, s3: herons_formula(s1, s2, s3),  # Uses heron's function to calculate area
                'perimeter': lambda s1, s2, s3: s1 + s2 + s3
            }
        }
    else:

        dimension_parameter_lists = parameter_3d_list_dict

        to_calculate_list = ['volume', 'surface area', 'both']

        # Dictionary mapping shapes to their parameters and prompts
        input_prompts = {
            'cuboid': {'length': ('length', 'Length: ', ''),
                       'width': ('width', 'Width: ', ''),
                       'height': ('height', 'Height: ', '')},

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
                'side1': ('side1', 'First side of triangle: ', ''),
                'side2': ('side2', 'Second side of triangle: ', ''),
                'side3': ('side3', 'Third side of triangle: ', ''),
                'height': ('height', 'Height: ', '')},
        }

        # Dictionary containing formulas for volume and surface area for each shape
        shape_calculations = {
            'cuboid': {
                'volume': lambda l, w, h: l * w * h,
                'surface area': lambda l, w, h: 2 * (l * w + l * h + w * h)
            },
            'cube': {
                'volume': lambda l: l ** 3,
                'surface area': lambda l: 6 * l ** 2
            },
            'cylinder': {
                'volume': lambda r, h: pi * r ** 2 * h,
                'surface area': lambda r, h: 2 * pi * r * h + 2 * pi * r ** 2
            },
            'triangular prism': {
                # Uses heron's function to help calculate
                'volume': lambda a, b, c, l: herons_formula(a, b, c) * l,
                'surface area': lambda a, b, c, l: 2 * herons_formula(a, b, c) + (a + b + c) * l
                },
            'cone': {
                'volume': lambda r, h: 1 / 3 * pi * r ** 2 * h,
                'surface area': lambda r, h: pi * r * (r + math.sqrt(h ** 2 + r ** 2))
            },
            'sphere': {
                'volume': lambda r: 4 / 3 * pi * r ** 3,
                'surface area': lambda r: 4 * pi * r ** 2
            },
            'square based pyramid': {
                'volume': lambda w, h: w ** 2 * h / 3,
                'surface area': lambda w, h: w ** 2 + w * math.sqrt((w / 2) ** 2 + h ** 2) * 2
            },
            'triangle based pyramid': {
                'volume': lambda a, b, c, h: 1 / 3 * herons_formula(a, b, c) * h,
                'surface area': lambda a, b, c, h: a + b + c + (math.sqrt(h ** 2 + (a / 2) ** 2) * 3)
                # regular tetrahedron
            }
        }

    # Retrieve prompts for user inputs associated with the chosen shape
    prompts = input_prompts[shape]

    # Create dictionary for user inputs needed for calculation
    inputs = {
        # Get user input for each parameter using prompts
        key: num_check(prompt[1], 0) for key, prompt in prompts.items()
    }

    # Check for impossible triangles
    if shape in ['triangle', 'triangle based pyramid', 'triangular prism']:
        # If the triangle is impossible output error and reset
        if not (inputs['side1'] + inputs['side2'] > inputs['side3'] and
                inputs['side1'] + inputs['side3'] > inputs['side2'] and
                inputs['side2'] + inputs['side3'] > inputs['side1']):
            print(color_text("The sides entered do not form a valid triangle.", 'red'))
            print()
            return

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
        # Add shape to shape_list for panda
        shape_2d_list.append(user_shape)
    else:
        panda_3d_dict.update(parameter_dict)
        # Add shape to shape_list for panda
        shape_3d_list.append(user_shape)

    # Calculate area / volume based on the chosen shape and user inputs
    answer_one = shape_calculations[shape][to_calculate_list[0]](*inputs.values())
    answer_one = round(answer_one, 2)

    # Calculate perimeter / surface area based on the chosen shape and user inputs
    answer_two = shape_calculations[shape][to_calculate_list[1]](*inputs.values())
    answer_two = round(answer_two, 2)

    print()

    # If user asked for area / volume or both then print answer one (area / volume)
    if to_calculate == to_calculate_list[0] or to_calculate == to_calculate_list[2]:
        print(f'{to_calculate_list[0]}: {answer_one}')

    # If user asked for perimeter / surface area or both then print answer two (perimeter / surface area)
    if to_calculate == to_calculate_list[1] or to_calculate == to_calculate_list[2]:
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


# Set up lists for string checker
yn_list = ['yes', 'no']
dimension_list = ['2d', '3d', 'xxx']
option_list_2d = ['area', 'perimeter', 'both']
option_list_3d = ['volume', 'surface area', 'both']

# set up valid shape lists including the word 'shapes'
shapes_2d = ['circle', 'square', 'rectangle', 'triangle']
shapes_3d = ['cuboid', 'cube', 'cylinder', 'triangular prism', 'cone',
             'sphere', 'square based pyramid', 'triangle based pyramid']

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

# Set up a list for 2d shapes used
shape_2d_list = []

# Create the dict used for the 2d panda
panda_2d_dict = {
    "Shape": shape_2d_list
}

# Set up a list for 3d shapes used
shape_3d_list = []

# Create the dict used for the 3d panda
panda_3d_dict = {
    "Shape": shape_3d_list
}

# list of items to write to file
to_write = []

print(color_text("<<<<< Welcome to the Super Shape Calculator! >>>>>", 'blue'))
print()

# Asks user if they want to read instructions, if yes output instructions
show_instructions = string_checker("Do you want to read the instructions? ", 1, yn_list)

if show_instructions == 'yes':
    instructions()


# Loop code until user quits
while True:

    # Asks user for a valid shape as per earlier choice
    user_shape = get_user_input()

    # If user enters 'xxx' quit
    if user_shape == 'xxx':
        break

    # Find out what dimension shape it is
    if user_shape in shapes_2d:
        dimensions = '2d'
    else:
        dimensions = '3d'

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
        panda_2d_dict.update(answer_2d_dict)

    # If 3d add the 3d answers
    else:
        panda_3d_dict.update(answer_3d_dict)


# If there is a 2d shape then make and set data
if len(shape_2d_list) > 0:
    print()
    subtitle_2d = "**** 2D Shapes ****\n"

    # Create the table frame for our data
    results_2d_frame = pandas.DataFrame(panda_2d_dict)

    # set index
    results_2d_frame = results_2d_frame.set_index('Shape')

    # convert dataframe to string
    table_2d = pandas.DataFrame.to_string(results_2d_frame)

    # Add to list to write to file
    to_write.append(subtitle_2d)
    to_write.append(table_2d)

    # Print out the data
    color_text(subtitle_2d, "blue")
    print(table_2d)

# If there is a 3d shape then make and set data
if len(shape_3d_list) > 0:
    print()
    subtitle_3d = "**** 3D Shapes ****\n"

    # Create the table frame for our data
    results_3d_frame = pandas.DataFrame(panda_3d_dict)

    # set index
    results_3d_frame = results_3d_frame.set_index('Shape')

    # convert dataframe to string
    table_3d = pandas.DataFrame.to_string(results_3d_frame)

    # Add to list to write to file
    to_write.append(subtitle_3d)
    to_write.append(table_3d)

    # print out the data
    color_text(subtitle_3d, "blue")
    print(table_3d)

# Ask if user wants to save data to file
write_to_file = string_checker("Do you want to save the data: ", 1, yn_list)

if write_to_file == 'yes':

    # Ask for file name
    file_name = input("File name: ")

    title = f"*** {file_name} ***\n\n"

    to_write.insert(0, title)

print()
print(color_text('Thank you for using the Super Shape Calculator', 'green'))
