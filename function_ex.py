#!/usr/bin/env python3

#function definition to convert a string to binary
def conv_binary(string):
    str_bytes = bytes(string, "ascii")
    binary_output = (' '.join(["{0:b}".format(x) for x in str_bytes]))
    return binary_output

#main program
run = 1                     #set run state to 1 'true'
while run == 1:             #while loop for run 
    user_input = str(input('Enter a word to convert to binary: ')) #user input
    binary_print = conv_binary(user_input)  #function call passing user input
    print(binary_print)                     #print result of converstion to binary
    
    #user prompt to continue running
    cont_prompt = str(input('Would you like to convert another word? (y/n): '))
    if (cont_prompt == 'n') or (cont_prompt == 'N'):    #no to end program  
        run = 0                                         #set run state to 0 'false'
    else:
        run = 1                                         #otherwise continue program