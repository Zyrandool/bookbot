from collections import Counter
import string

def get_num_words(text):
    """Count the number of words in the given text."""
    return len(str.split(text))

def clear_punctuation(text):
    """Remove punctuation from the given text."""
    for char in string.punctuation:
        text = text.replace(char, "")
    return text

def get_char_number(text):
    """Count the number of each character in the given text, ignoring case."""
    lowertext = str.lower(text)
    char_count = {}
    for character in lowertext:
        if(character in char_count):
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1
    return char_count

def average_word_length(text):
    """Calculate the average word length in characters from the given text."""
    text = clear_punctuation(text)
    text = str.lower(text)
    words = str.split(text)
    if len(words) == 0:
        return 0
    total_length = 0
    for word in words:  
        total_length += len(word)
    return total_length / len(words)

def get_most_frequent_words(text, stop_words=None):
    """Count the most frequent words in the given text, excluding stop words."""
    if stop_words is None:
        stop_words = []
    
    text = clear_punctuation(text)
    text = str.lower(text)
    words = str.split(text)
    
    filtered_words = []
    for word in words:
        if word != "" and word not in stop_words:
            filtered_words.append(word)
    return Counter(filtered_words)

def get_num_unique_words(text):
    """Count the number of unique words in the given text."""
    text = clear_punctuation(text)
    text = str.lower(text)
    words = str.split(text)
    if not words:
        return 0
    unique_words_set = set()
    for word in words:
        if word:
            unique_words_set.add(word)
    return len(unique_words_set)

def get_longest_shortest_words(text):
    """Find the longest and shortest words in the given text."""
    text = clear_punctuation(text)
    text = str.lower(text)
    list_after_split = str.split(text)
    words = []
    for word in list_after_split:
        if word:
            words.append(word)
    if not words:
        return "", ""
    
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    return longest_word, shortest_word

def get_average_sentence_length(text):
    """Calculate the average sentence length in words from the given text."""
    processed_text = text.replace('!', '.').replace('?', '.')
    potential_sentences_list = processed_text.split('.')
    sentences = []
    for sentence_candidate in potential_sentences_list:
        stripped_candidate = sentence_candidate.strip()
        if stripped_candidate:
            sentences.append(stripped_candidate)

    # Assign the list of cleaned sentences.
    if not sentences:
        return 0
    
    total_words_in_sentences = 0
    for sentence in sentences:
        words_in_sentence = len(str.split(clear_punctuation(sentence)))
        total_words_in_sentences += words_in_sentence
        
    return total_words_in_sentences / len(sentences)

def display_stats(num_words, char_count, average_length, frequent_words, num_unique_words, longest_word, shortest_word, avg_sentence_len):
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    print("----------- Stats ----------")
    print(f"Found {num_words} total words")
    print(f"Found {num_unique_words} unique words")
    print("----------------------------")
    print(f"Average word length: {average_length:.2f} characters")
    print(f"Average sentence length: {avg_sentence_len:.2f} words")
    print(f"Longest word: '{longest_word}' ({len(longest_word)} chars)")
    print(f"Shortest word: '{shortest_word}' ({len(shortest_word)} chars)")
    print("-------- Character Count --------")
    for char, count in sorted_chars:
        if(char.isalpha()):
            print(f"{char}: {count}")
    print("-------- Most Frequent Words --------")
    # Display top 10 most frequent words, for example
    for word, count in frequent_words.most_common(10):
        print(f"{word}: {count}")

