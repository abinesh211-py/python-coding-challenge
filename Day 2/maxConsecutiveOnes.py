def maxConcOnes():
    arr = list(map(int, input("Enter the binary array elements separated by space (only 0s and 1s): ").split()))
    count = max_count = 0
    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    print("Maximum consecutive ones are:", max_count)
maxConcOnes()