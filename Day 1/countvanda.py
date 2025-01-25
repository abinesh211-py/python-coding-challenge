#finding the count of vowels and consonants
def count_v_c(s):
    vowels = "aeiouAEIOU"
    counts = {"vowels": 0, "consonants": 0}
    for char in s:
        if char.isalpha():
            if char in vowels:
                counts["vowels"] += 1
            else:
                counts["consonants"] += 1
    return counts

s = input("Enter a string: ")
print(f"The counts are {count_v_c(s)}")