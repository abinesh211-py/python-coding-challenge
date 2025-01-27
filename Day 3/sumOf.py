# Input dimensions of the matrices
rows = int(input("Enter the number of rows in the matrices: "))
cols = int(input("Enter the number of columns in the matrices: "))

# Input the first matrix
print("Enter elements for the first matrix row by row:")
matrix1 = []
for i in range(rows):
    while True:
        row = list(map(int, input(f"Enter row {i + 1} ({cols} elements): ").split()))
        if len(row) == cols:
            matrix1.append(row)
            break
        else:
            print(f"Please enter exactly {cols} elements!")

# Input the second matrix
print("Enter elements for the second matrix row by row:")
matrix2 = []
for i in range(rows):
    while True:
        row = list(map(int, input(f"Enter row {i + 1} ({cols} elements): ").split()))
        if len(row) == cols:
            matrix2.append(row)
            break
        else:
            print(f"Please enter exactly {cols} elements!")

# Add the two matrices
result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Print the resultant matrix
print("Resultant Matrix after addition:")
for row in result:
    print(" ".join(map(str, row)))
