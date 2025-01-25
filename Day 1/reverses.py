# reversing  String Using Loop
def revered_S(s):
    rev_s = ""
    for char in s:
        rev_s = char + rev_s
    return rev_s
s=input("Enter the string:")
print(f"The reversed string is : {revered_S(s)}") 
