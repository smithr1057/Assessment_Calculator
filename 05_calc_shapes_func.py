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


# Calculates
def calc_shape(user_choice):

    if user_choice == '2d':

        two_answers =

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
    prompts = input_prompts[user_choice]

    # Create dictionary for user inputs needed for area calculation
    inputs = {
        # Get user input for each parameter then iterate over parameter and prompt
        key: num_check(prompt[1], 0)
        for key, prompt in prompts.items()
    }

    if area_perimeter in ['area', 'both']:
        # Calculate area based on the chosen shape and user inputs
        area = shape_calculations[user_choice]['area'](*inputs.values())

    if area_perimeter in ['perimeter', 'both']:
        # Calculate perimeter based on the chosen shape and user inputs
        perimeter = shape_calculations[user_choice]['perimeter'](*inputs.values())

    print()
    if area_perimeter in ['area', 'both']:
        print(f'Area: {area:.2f}')
    if area_perimeter in ['perimeter', 'both']:
        print(f'Perimeter: {perimeter:.2f}')
    print()

