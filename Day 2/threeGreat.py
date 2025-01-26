def threeGreat():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    if len(arr) < 3:
        print("Array must contain at least three elements.")
        return

    first = second = third = float('-inf')
    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num

    print("Three greatest elements are:", [first, second, third])
threeGreat()