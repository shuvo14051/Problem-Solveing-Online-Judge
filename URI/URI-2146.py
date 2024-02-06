while True:
    try:
        # Read input until the end of the file
        num = input()
        
        # Check if the input is not empty
        if num:
            # Convert the input to an integer, subtract 1, and print the result
            result = int(num) - 1
            print(result)
    except EOFError:
        # Exit the loop when the end of the file is reached
        break
