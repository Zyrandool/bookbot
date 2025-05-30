from collections import defaultdict
import string

def get_num_words(text):
    return len(str.split(text))

def clear_punctuation(text):
    for char in string.punctuation:
        text = text.replace(char, "")
    return text

def get_char_number(text):
    lowertext = str.lower(text)
    char_count = {}
    for character in lowertext:
        if(character in char_count):
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1
    return char_count

def average_word_length(text):
    text = clear_punctuation(text)
    text = str.lower(text)
    words = str.split(text)
    if len(words) == 0:
        return 0
    total_length = 0
    for word in words:  
        total_length += len(word)
    return total_length / len(words)

def display_stats(num_words, char_count, average_length):
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    print("----------- Stats ----------")
    print(f"Found {num_words} total words")
    print("----------------------------")
    print(f"Average word length: {average_length:.2f} characters")
    print("-------- Character Count --------")
    for char, count in sorted_chars:
        if(char.isalpha()):
            print(f"{char}: {count}")

