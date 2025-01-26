def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
arr=[12,242,14,341,43,1]
print(f"The min value and maximum value is :{find_max_min(arr)}")