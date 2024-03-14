import colorama
# Functions


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
        print(colorama.Fore.RED + error + colorama.Fore.RESET)
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
                    print(colorama.Fore.RED + f"Please enter a number between {low} and {high}" + colorama.Fore.RESET)
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response <= low:
                    print(colorama.Fore.RED + f"Please enter a number that is more than {low}" + colorama.Fore.RESET)
                    continue

            return response

        except ValueError:
            print(colorama.Fore.RED + "Please enter a number" + colorama.Fore.RESET)
            continue


def print_valid_shapes(dim, shape_list):
    print(f"*** Valid {dim} Shapes ***")
    print(", ".join(shape_list))


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
            return f"You picked {shape}"


# Main Routine
# Lists
dimension_list = ['2d', '3d']


while True:
    dimension = string_checker('2D or 3D shape? ', 1, ['2d', '3d'])

    if dimension == '2d':
        user_choice = get_user_input('2d')
    else:
        user_choice = get_user_input('3d')



