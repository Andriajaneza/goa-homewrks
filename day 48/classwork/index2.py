import random # import the random

def random_name(): # make function of everything
        empy_string = "" # make empty string for place characters in here
        my_name = "a n d r i a" # chosse name we want to spilt
        my_name_spilt = my_name.split() # spilt the name to list of characters
        for char in my_name_spilt: # make for loop for add every character
            random_char = random.choice(my_name_spilt) # chosse random characters from name
            empy_string += random_char # add chossed characters to empty string on ln 4
            my_name_spilt.remove(random_char) # remove the chossed character because dont chosse it more
        return empy_string # and in final print full string

print(random_name()) # do function to work this code 