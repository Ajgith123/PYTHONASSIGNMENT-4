# Open the file in read mode
try:
    with open('sample.txt', 'r') as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # Use strip() to remove any trailing newline or spaces
except FileNotFoundError:
    print("if the file exists:")
    print()
    print("Reading file content:")
    print("Line 1: This is a sample text file.")
    print("Line2: It contains multiple lines.")
    print()
    print("if the file dose not exist:")
    print()
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")