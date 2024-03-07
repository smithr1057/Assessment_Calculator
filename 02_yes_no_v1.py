
show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()
    print()

    # If they say yes, output "program continues"
    program_cont = ["yes", "y"]

    # If they say no , output 'display instructions'
    instructions = ["no", "n"]

    if show_instructions in program_cont:
        print("Program continues")
        print()

    elif show_instructions in instructions:
        print("***INSTRUCTIONS***")
        print()

    # If they say anything else then 'error please enter yes / no'
    else:
        print(" **ERROR** please enter either yes / no")
        print()