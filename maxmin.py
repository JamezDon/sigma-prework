#int_list = [-100,100]

max = int_list[0]
min = int_list[0]
for number in int_list:
    if number > max:
        max = number
    elif number < min:
        min = number

print([min,max])
