rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []

print("Enter the matrix row by row:")

# Loop through the rows and take input for each row
for i in range(rows):
    while True:
        row = input(f"Enter exactly {cols} elements for row {i + 1}, separated by spaces: ").split()
        
        # Check if the number of elements in the row matches the number of columns
        if len(row) == cols:
            matrix.append(list(map(int, row)))  # Convert to integers and add the row to the matrix
            break  # Exit the loop if the input is valid
        else:
            print(f"Invalid input! Please enter exactly {cols} elements.")

# Print the matrix
print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

# Find the maximum element in the matrix
max_element = float('-inf')

# Traverse through the matrix to find the maximum element
for row in matrix:
    for element in row:
        if element > max_element:
            max_element = element

# Print the maximum element
print("Maximum element in the matrix:", max_element)
