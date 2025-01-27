# Input dimensions
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

# Input the matrix
matrix = []
for i in range(rows):
    while True:
        row = list(map(int, input(f"Enter row {i + 1} ({cols} elements): ").split()))
        if len(row) == cols:
            matrix.append(row)
            break
        else:
            print(f"Please enter exactly {cols} elements!")

# Calculate row sums
row_sums = [sum(row) for row in matrix]

# Calculate column sums
column_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]

# Print results
print("Row sums:", row_sums)
print("Column sums:", column_sums)
