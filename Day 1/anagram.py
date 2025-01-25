#Checking for anagram
def anag_counting(str1, str2):
    if len(str1) != len(str2):
        return False
    count1 = {}
    count2 = {}
    for char in str1:
        count1[char] = count1.get(char, 0) + 1
    for char in str2:
        count2[char] = count2.get(char, 0) + 1
    return count1 == count2
str1=input("Enter first string: ")
str2= input("Enter the Second word: ")
print(f"The anargram checking of {str1},{str2} is {anag_counting(str1,str2)}")