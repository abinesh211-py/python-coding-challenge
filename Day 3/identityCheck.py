# Input the size of the square matrix
n = int(input("Enter the size of the square matrix (n x n): "))

# Input the matrix
print(f"Enter the elements of the {n}x{n} matrix row by row:")
matrix = []
for i in range(n):
    while True:
        row = list(map(int, input(f"Enter row {i + 1} ({n} elements): ").split()))
        if len(row) == n:
            matrix.append(row)
            break
        else:
            print(f"Please enter exactly {n} elements!")

# Check if it's an identity matrix
is_identity = all(
    matrix[i][j] == (1 if i == j else 0)
    for i in range(n) for j in range(n)
)

# Print the result
if is_identity:
    print("The matrix is an identity matrix.")
else:
    print("The matrix is not an identity matrix.")
