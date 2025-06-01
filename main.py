from stats import *
from sys import argv, exit 

def get_book_text(filepath):
    try:
        f = open(filepath, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: The file {filepath} does not exist.")
        exit(1)
    else:
        with f:
            # Read the entire file content
            return f.read()

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    filepath=argv[1]
    if not filepath.endswith('.txt'):
        print("Please provide a valid text file.")
        exit(1)
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_count = get_char_number(text)
    average_length = average_word_length(text)
    stop_words = ["the", "a", "is", "in", "it", "of", "and", "to", "or", "s", "in", "that", "this", "for", "with", "as", "was", "on", "at", "by", "an", "be", "are", "not", "from", "but", "all", "if", "so"]
    frequent_words = get_most_frequent_words(text, stop_words=stop_words)
    num_unique_words = get_num_unique_words(text) 
    longest_word, shortest_word = get_longest_shortest_words(text)
    avg_sentence_len = get_average_sentence_length(text)

    print("============ BOOKBOT ============")
    print(f"Reading book from {filepath}")
    print("=================================")
    display_stats(num_words, char_count, average_length, frequent_words, num_unique_words, longest_word, shortest_word, avg_sentence_len)

# Dodaj to wywołanie funkcji main()
if __name__ == "__main__":
    main()
