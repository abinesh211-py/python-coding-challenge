#this is split and join with build in
def string_split_join(line):
    words = line.split()
    result = '-'.join(words)
    return result
line = input("Enter the Line:")
result = string_split_join(line)
print(f"The string Given : {line}")
print(f"String after joining: {result}")
