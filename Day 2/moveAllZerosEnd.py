def moveAllZeros():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    count = 0  # Count of non-zero elements

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

    print("Array after moving all zeroes to the end:", arr)
moveAllZeroes()