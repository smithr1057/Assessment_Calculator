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
shape_formulas = {
    'circle': {'area': lambda r: math.pi * r ** 2, 'perimeter': lambda r: 2 * math.pi * r},
    'square': {'area': lambda s: s ** 2, 'perimeter': lambda s: 4 * s},
    'rectangle': {'area': lambda l, w: l * w, 'perimeter': lambda l, w: 2 * (l + w)},
    'triangle': {'area': lambda b, h: 0.5 * b * h, 'perimeter': lambda s1, s2, s3: s1 + s2 + s3}
}

# Main Routine
area_perm_list = ['area', 'perimeter', 'both']
pi = math.pi

while True:
    area = perimeter = 0
    user_choice = get_user_input('2d')
    area_perimeter = string_checker("Do you want area, perimeter or both calculated? ", area_perm_list,
                                    "Please choose 'area', 'perimeter' or 'both'")

    if user_choice in shape_formulas:
        prompts = input_prompts[user_choice]
        if area_perimeter in ['area', 'both']:
            inputs = {key: num_check(prompt[1], 0) for key, prompt in prompts.items() if
                      key != 'side1' and key != 'side2' and key != 'side3'}
            if user_choice == 'triangle':
                inputs['base'] = inputs.pop('side1')
                inputs['height'] = inputs.pop('side2')
            area = shape_formulas[user_choice]['area'](**inputs)

        if area_perimeter in ['perimeter', 'both']:
            if user_choice == 'triangle':
                inputs = {key: num_check(prompt[1], 0) for key, prompt in prompts.items() if
                          key != 'base' and key != 'height'}
                inputs['s1'] = inputs.pop('side1')
                inputs['s2'] = inputs.pop('side2')
                inputs['s3'] = inputs.pop('side3')
            else:
                inputs = {key: num_check(prompt[1], 0) for key, prompt in prompts.items()}
            perimeter = shape_formulas[user_choice]['perimeter'](**inputs)

    print()
    if area_perimeter in ['area', 'both']:
        print(f'Area: {area:.2f}')
    if area_perimeter in ['perimeter', 'both']:
        print(f'Perimeter: {perimeter:.2f}')
    print()
