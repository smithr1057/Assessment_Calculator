import pandas

# Set up lists and dictionaries
shape_list = []
length_list = []
area_list = []

variable_dict = {
    "Shape": shape_list,
    "Length": length_list,
    "area": area_list
}

whats_calculated_list = ['area', 'perimeter', 'both']
parameter_list = []
while True:
    shape = input('Shape: ')
    if shape == 'xxx':
        break
    # while True:
    #     parameter = input('Parameters: ')
    #     if parameter == 'xxx':
    #         break
    #     parameter_list.append(parameter)
    length = input('length: ')
    # whats_calculated = input('Whats calculated? ')
    area = input('area: ')

    shape_list.append(shape)
    length_list.append(length)
    area_list.append(area)

# Create the table frame for our data
results_frame = pandas.DataFrame(variable_dict)

# set index
expense_frame = results_frame.set_index('Shape')

print(expense_frame)
