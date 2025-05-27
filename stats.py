from collections import defaultdict

def get_num_words(text):
    return len(str.split(text))

def get_char_number(text):
    lowertext = str.lower(text)
    char_count = {}
    for character in lowertext:
        if(character in char_count):
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1
    return char_count

def display_stats(num_words, char_count):
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for char, count in sorted_chars:
        if(char.isalpha()):
            print(f"{char}: {count}")

