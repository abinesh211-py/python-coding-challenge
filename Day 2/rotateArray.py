def rotate_array():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    k = int(input("Enter the number of rotations: "))
    k %= len(arr)  
    arr[:] = arr[-k:] + arr[:-k]  
    print("Array after rotation:", arr)
rotate_array()