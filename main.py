from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath="books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_count = get_char_number(text)
    print(f"{num_words} words found in the document")
    print(char_count)



# Dodaj to wywołanie funkcji main()
if __name__ == "__main__":
    main()
