#Checking the given is palindrome or not
def palindrom(s):
    cleaned = ''
    for char in s:
        if char.isalnum():  
            cleaned += char.lower()  

    reversed_c = cleaned[::-1]  
    return cleaned == reversed_c 

s = input("Enter the string: ")
print(f"The given {s} is {palindrom(s)}")
