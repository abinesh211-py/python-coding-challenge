#Split and join without using inbuild function

def Split_join(line):
    words = []
    word = ""
    for char in line:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word:
        words.append(word)

    result = ""
    for i in range(len(words)):  # Fixed the indentation here
        if i != 0:
            result += "-"
        result += words[i]
    return result

line = input("Enter the string: ")
print(Split_join(line))
print(f"The joined string is: {Split_join(line)}")
