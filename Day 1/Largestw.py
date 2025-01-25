#Finding the largest word 
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word
    return longest

sentence = input("Enter the Sentence: ")
print(f"The longest word from the sentence is '{longest_word(sentence)}'")
