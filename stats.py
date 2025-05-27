from collections import defaultdict

def get_num_words(text):
    return len(str.split(text))

def get_char_number(text):
    l = str.lower(text)
    char_count = defaultdict(int)
    for char in l:
        char_count[l]+=1
    return char_count