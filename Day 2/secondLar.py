def second_largest_element():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))

    if len(arr) < 2:
        print("Array must contain at least two elements.")
        return
    
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    if second == float('-inf'):
        print("No second largest element.")
    else:
        print("Second largest element is:", second)
second_largest_element()