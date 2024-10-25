def create_and_modify_list():
    # Generate a list of 10 random integers between -50 and 50
    numbers = [1,4,2,7,8,4,100,12,45,363463]
    
    print("Original list:", numbers)
    
    # Find the lowest number in the list
    lowest_number = min(numbers)
    
    # Create a new list starting with the lowest number + 100, followed by the original numbers
    modified_list = [lowest_number + 100] + numbers
    
    # Sort the modified list in ascending order
    modified_list.sort()
    
    # Print the final sorted list
    print("Modified list:", modified_list)

create_and_modify_list()
