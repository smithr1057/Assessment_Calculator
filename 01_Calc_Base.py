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
        print(colorama.Fore.RED + error)
        print()


# Displays instructions
def instructions():
    return "*** Instructions ***"


# Main Routine
# Lists
yn_list = ['yes', 'no']
dimension_list = ['2d', '3d']
shapes_2d = ['circle', 'square', 'rectangle', 'triangle', 'shapes']
shapes_3d = ['cuboid', 'cylinder', 'triangular prism', 'cone',
             'sphere', 'square based pyramid', 'triangle based pyramid', 'shapes']

# Asks user if they want to read instructions, if yes output instructions
show_instructions = string_checker("Do you want to read the instructions? ", 1, yn_list)

if show_instructions == 'yes':
    instructions()

# Loop code until user quits
while True:
    pass
