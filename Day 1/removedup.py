#removing the duplicates
def remove_dup(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result 
s=input("Enter the string: ")
print(f"The duplicates from {s} is {remove_dup(s)}")