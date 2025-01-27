# Input dimensions of the matrix
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

# Input the matrix
print("Enter the elements of the matrix row by row:")
matrix = []
for i in range(rows):
    while True:
        row = list(map(int, input(f"Enter row {i + 1} ({cols} elements): ").split()))
        if len(row) == cols:
            matrix.append(row)
            break
        else:
            print(f"Please enter exactly {cols} elements!")

# Count zeros
zero_count = sum(row.count(0) for row in matrix)

# Print the count of zeros
print(f"The number of zeros in the matrix: {zero_count}")
