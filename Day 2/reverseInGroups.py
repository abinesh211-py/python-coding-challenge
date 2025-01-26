def reverseInGroups():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    k = int(input("Enter the group size: "))

    for i in range(0, len(arr), k):
        arr[i:i + k] = reversed(arr[i:i + k])

    print("Array after reversing in groups:", arr)

reverseInGroups()