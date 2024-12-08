def string_to_array(input_string):
    """
    Splits a given string into an array of words, ensuring special cases like empty strings are handled.
    
    :param input_string: The string to split
    :return: A list of words or [''] if the input is empty
    """
    if input_string == "":
        return [""]
    return input_string.split()

# Example usage
example_string = ""
result = string_to_array(example_string)
print("Result:", result)