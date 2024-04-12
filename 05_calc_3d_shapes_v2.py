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
    print(", ".join(shape_list[:-1]))  # Exclude 'shapes'


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

# Dictionary mapping shapes to their parameters and prompts
input_prompts_3d = {
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
shape_formulas_3d = {
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
        'surface area': lambda a, b, c, l: l * (a + b + c) + 1 / 4 * ((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)) ** 0.5 + 1 / 4 * ((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)) ** 0.5
    },
    'cone': {
        'volume': lambda r, h: 1/3 * pi * r ** 2 * h,
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


# Lists
vol_face_list = ['volume', 'surface area', 'both']

# Set pi value
pi = math.pi

# Loop code until user quits
while True:

    volume = surface_area = 0

    user_choice = get_user_input('3d')
    print()
    vol_face = string_checker('Do you want the volume, surface area or both calculated? ', 1, vol_face_list)

    if user_choice in shape_formulas_3d:
        # Retrieve prompts for user inputs associated with the chosen shape
        prompts = input_prompts_3d[user_choice]

        # Create dictionary for user inputs needed for area calculation
        inputs = {
            # Get user input for each parameter then iterate over parameter and prompt
            key: num_check(prompt[1], 0)
            for key, prompt in prompts.items()
        }

        if vol_face in ['volume', 'both']:
            # Calculate area based on the chosen shape and user inputs
            volume = shape_formulas_3d[user_choice]['volume'](*inputs.values())

        if vol_face in ['surface area', 'both']:
            # Calculate perimeter based on the chosen shape and user inputs
            surface_area = shape_formulas_3d[user_choice]['surface area'](*inputs.values())
    print()

    # Output the necessary answers
    if vol_face in ['volume', 'both']:
        print(f'Volume: {volume:.2f}')
    if vol_face in ['surface area', 'both']:
        print(f'Surface Area: {surface_area:.2f}')
    print()
