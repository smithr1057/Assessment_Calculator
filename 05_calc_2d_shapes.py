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
area_perm_list = ['area', 'perimeter', 'both']


# Set pi value
pi = math.pi

# Loop code until user quits
while True:

    # reset area and perimeter to 0
    area = 0
    perimeter = 0

    # ask user what they want calculated
    user_choice = get_user_input('2d')
    area_perimeter = string_checker("Do you want area, perimeter or both calculated? ", 1, area_perm_list)

    if user_choice == 'circle':
        # Ask user for required information Then calculate area / perimeter
        radius = num_check('Enter radius of the circle (half the diameter): ', 0)

        area = pi * radius ** 2
        perimeter = 2 * pi * radius

    elif user_choice == 'square':
        # Ask user for required information Then calculate area / perimeter
        length = num_check('Enter length of the square: ', 0)

        area = length ** 2
        perimeter = 4 * length

    elif user_choice == 'rectangle':
        # Ask user for required information Then calculate area / perimeter
        length = num_check('Enter length of the rectangle: ', 0)
        width = num_check('Enter width of the rectangle: ', 0)

        area = length * width
        perimeter = 2 * (length + width)

    else:
        # Ask user for required information Then calculate area / perimeter
        if area_perimeter == 'area':
            base = num_check('Enter base of the triangle: ', 0)
            height = num_check('Enter height of the triangle: ', 0)
            area = 0.5 * base * height
        # if perimeter is needed then use herons equation for area
        else:
            s1 = num_check('Enter the length of one of the sides: ', 0)
            s2 = num_check('Enter the length of a different side: ', 0)
            s3 = num_check('Enter the length of the last side: ', 0)
            perimeter = s1 + s2 + s3
            s = perimeter / 2
            area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

    print()

    if area_perimeter == 'area':
        print(f'Area: {area:.2f}')

    elif area_perimeter == 'perimeter':
        print(f'Perimeter: {perimeter:.2f}')

    else:
        print(f'Area: {area:.2f}')
        print(f'Perimeter: {perimeter:.2f}')
    print()
