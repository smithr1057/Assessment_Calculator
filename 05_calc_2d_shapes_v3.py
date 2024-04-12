# V3 - Fixed ChatGPTs broken code and removed some unnecessary code
import math


# Function to change text color
def color_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    print(f"{colors.get(color, '')}{text}\033[0m")


# Function to check string input
def string_checker(question, valid_list, custom_error=None):
    error = custom_error or f"Please choose {' or '.join(valid_list)}"
    while True:
        response = input(question).lower()
        if response in valid_list:
            return response
        color_text(error, 'red')
        print()


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


# Function to print valid shapes
def print_valid_shapes(dim, shape_list):
    print(f"*** Valid {dim} Shapes ***")
    print(", ".join(shape_list))


# Function to get user input for shape
def get_user_input(var_dimension):
    shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes']
    shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone', 'sphere', 'square based pyramid',
                 'triangle based pyramid', 'shapes']
    while True:
        shape_list = shapes_2d if var_dimension == '2d' else shapes_3d
        shape = string_checker(f"Enter the shape you want (or 'shapes' to see valid options): ", shape_list,
                               f"Please enter a valid shape, or enter 'shapes' to see the valid options.")
        if shape == 'shapes':
            print_valid_shapes(var_dimension, shapes_2d if var_dimension == '2d' else shapes_3d)
        else:
            return shape


# Main Routine

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
shape_2d_calculations = {
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

area_perm_list = ['area', 'perimeter', 'both']
pi = math.pi

while True:
    # reset answer values
    area = perimeter = 0

    # Ask user for shape and area, perimeter or both
    user_choice = get_user_input('2d')
    print()
    area_perimeter = string_checker("Do you want area, perimeter or both calculated? ", area_perm_list,
                                    "Please choose 'area', 'perimeter' or 'both'")

    if user_choice in shape_2d_calculations:
        # Retrieve prompts for user inputs associated with the chosen shape
        prompts = input_prompts[user_choice]

        # Create dictionary for user inputs needed for area calculation
        inputs = {
            # Get user input for each parameter then iterate over parameter and prompt
            key: num_check(prompt[1], 0)
            for key, prompt in prompts.items()
        }

        if area_perimeter in ['area', 'both']:
            # Calculate area based on the chosen shape and user inputs
            area = shape_2d_calculations[user_choice]['area'](*inputs.values())

        if area_perimeter in ['perimeter', 'both']:
            # Calculate perimeter based on the chosen shape and user inputs
            perimeter = shape_2d_calculations[user_choice]['perimeter'](*inputs.values())

    print()
    if area_perimeter in ['area', 'both']:
        print(f'Area: {area:.2f}')
    if area_perimeter in ['perimeter', 'both']:
        print(f'Perimeter: {perimeter:.2f}')
    print()
