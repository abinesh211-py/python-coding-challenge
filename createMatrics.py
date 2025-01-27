rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the matrix row by row:")

for i in range(rows):
    while True:
        row = input(f"Enter exactly {cols} elements for row {i + 1}, separated by spaces: ").split()
        if len(row) == cols:
            matrix.append(list(map(int, row))) 
            break
        else:
            print(f"Invalid input! Please enter exactly {cols} elements.")
print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))
