def arraySum(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print("Sum of the array:", arraySum(arr))
arraySum(arr)
