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

# Extract the diagonals
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

# Print the diagonals
print("Primary Diagonal:", " ".join(map(str, primary_diagonal)))
print("Secondary Diagonal:", " ".join(map(str, secondary_diagonal)))
