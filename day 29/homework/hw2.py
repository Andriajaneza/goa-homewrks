def classify_numbers():
    numbers = []
    results = []
    
    # Ask the user for 10 numbers
    for i in range(10):
        while True:
            try:
                num = int(input(f"Please enter number {i + 1}: "))
                numbers.append(num)
                break  # Break the loop if input is valid
            except ValueError:
                print("That's not a valid integer. Please try again.")

    # Classify each number
    for num in numbers:
        if num == 0:
            results.append(0)
        elif num % 2 == 0:
            results.append("even")
        else:
            results.append("odd")

    # Print the results
    print("The classification of the numbers is:", results)

classify_numbers()