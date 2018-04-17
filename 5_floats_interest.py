#!/usr/bin/env python3

import decimal
float_list = []
separator = '======================='

#instructions
print ('Enter five floating-point values: \nex. 3.14 or 2.22\n')

#user input loop
for index in range(1,6):
    user_input = float(input("{0}: " .format(index)))
    float_list.append(user_input)
    index += 1

#calculations
print('{0}' .format(separator))
print ('Total: \t\t {0:>10.2f}' .format(sum(float_list)))
print ('Average: \t {0:>10.2f}' .format((sum(float_list))/5))
print ('Maximum: \t {0:>10.2f}' .format(max(float_list)))
print ('Minimum: \t {0:>10.2f}' .format(min(float_list)))

#interest title
print('{0}' .format(separator))
print('{0:^23}' .format('Interest at 20%'))
print('{0}' .format(separator))

#print interest loop
for count, value in enumerate(float_list):
    interest = (value + (value*.2))
    print('{0}:\t\t\t{1:>11.2f}' .format(count+1, interest))
    count += 1