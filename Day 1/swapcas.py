def swapcase(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
s = input("Enter the string :")
print(swapcase(s))
print(f"Given String is :{s}")
print(f"The Swapped string is :{swapcase(s)}")