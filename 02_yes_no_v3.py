# Functions
# checks user answers with valid answer
def string_checker(question, num_letters, valid_list):

    error = f"Please choose {valid_list[0]} or {valid_list[1]}"

    while True:

        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for i in valid_list:
            if response == i[:num_letters] or response == i:
                return i

        # output error if item not in list
        print(error)
        print()


# Main Routine

# lists
yn_list = ['yes', 'no']

while True:
    show_instructions = string_checker("Do you want to read the instructions? ", 1, yn_list)

    if show_instructions == 'yes':
        print("*** Instructions ***")

    print('Program Continues')
    print()
