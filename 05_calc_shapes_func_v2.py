import math

pi = math.pi


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


def herons_formula(a, b, c):
    # Calculate area of triangle with heron's formula
    s = (a + b + c) / 2  # semi perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Calculates shapes area and perimeter /
# volume and surface area and prints out the answer
def calc_shape(shape, dimension, to_calculate):
    # Set up the parameter dictionary
    parameter_dict = {}

    # Common prompts
    prompt_dict = {
        'radius': ('radius', 'Radius: ', ''),
        'length': ('length', 'Length: ', ''),
        'width': ('width', 'Width: ', ''),
        'height': ('height', 'Height: ', ''),
        'side1': ('side1', 'First side: ', ''),
        'side2': ('side2', 'Second side: ', ''),
        'side3': ('side3', 'Third side: ', '')
    }

    # Set input prompts and shape calculations
    if dimension == '2d':

        to_calculate_list = ['area', 'perimeter', 'both']

        # Dictionary linking shape to its prompt
        input_prompts = {
            'circle': ['radius'],
            'square': ['length'],
            'rectangle': ['length', 'width'],
            'triangle': ['side1', 'side2', 'side3']
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

        to_calculate_list = ['volume', 'surface area', 'both']

        # ********* MORE EFFICIENT DICTIONARIES REPEATED CODE ******************

        # Dictionary linking shape to its prompt
        input_prompts = {
            'cuboid': ['length', 'width', 'height'],
            'cube': ['length'],
            'cylinder': ['radius', 'height'],
            'triangular prism': ['side1', 'side2', 'side3', 'length'],
            'cone': ['radius', 'height'],
            'sphere': ['radius'],
            'square based pyramid': ['width', 'height'],
            'triangle based pyramid': ['side1', 'side2', 'side3', 'height']
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
    prompts = {key: prompt_dict[key] for key in input_prompts[shape]}

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

    print()


# Main Routine
calc_shape('square', '2d', 'both')
