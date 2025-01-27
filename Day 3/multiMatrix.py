print("BOTH MATIX SHOULD HAVE SAME NUMBER OF ELEMENTS")
# Input dimensions for two matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Validate dimensions for multiplication
if cols1 != rows2:
    print("Matrix multiplication not possible!")
else:
    # Input first matrix
    print("Enter elements for the first matrix:")
    matrix1 = []
    for i in range(rows1):
        while True:
            row = list(map(int, input(f"Enter row {i + 1} ({cols1} elements): ").split()))
            if len(row) == cols1:
                matrix1.append(row)
                break
            else:
                print(f"Please enter exactly {cols1} elements!")

    # Input second matrix
    print("Enter elements for the second matrix:")
    matrix2 = []
    for i in range(rows2):
        while True:
            row = list(map(int, input(f"Enter row {i + 1} ({cols2} elements): ").split()))
            if len(row) == cols2:
                matrix2.append(row)
                break
            else:
                print(f"Please enter exactly {cols2} elements!")

    # Initialize the result matrix
    result = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Print the result matrix
    print("Resultant Matrix:")
    for row in result:
        print(" ".join(map(str, row)))
