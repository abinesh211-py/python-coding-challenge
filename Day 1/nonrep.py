def first_non_repeating(s: str) -> str:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return ''  


s = input("Enter a string: ")
print(f"The first non-repeating character in '{s}' is '{first_non_repeating(s)}'")
