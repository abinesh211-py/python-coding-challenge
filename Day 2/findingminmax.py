def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

if len(arr) < 2:
    print("Array must have at least 2 elements.")
else:
    max_val,min_val = find_max_min(arr)
    print(f"The min value is {min_val} and maximum value is: {max_val}")
