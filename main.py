from stats import *
from sys import argv, exit 

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath=argv[1]
    if not filepath.endswith('.txt'):
        print("Please provide a valid text file.")
        sys.exit(1)
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_count = get_char_number(text)
    print("============ BOOKBOT ============")
    print(f"Reading book from {filepath}")
    print("=================================")
    display_stats(num_words, char_count)


# Dodaj to wywołanie funkcji main()
if __name__ == "__main__":
    main()
