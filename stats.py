from collections import Counter
import string
from typing import Dict, List, Optional, Tuple

def get_num_words(text: str) -> int:
    """Counts the number of words in the given text.

    Args:
        text: The input string.

    Returns:
        The total number of words.
    """
    return len(text.split())

def clear_punctuation(text: str) -> str:
    """Removes all punctuation characters from the given text.

    Args:
        text: The input string.

    Returns:
        The text with punctuation removed.
    """
    for char in string.punctuation:
        text = text.replace(char, "")
    return text

def get_char_number(text: str) -> Dict[str, int]:
    """Counts the occurrences of each character in the text, ignoring case.

    Args:
        text: The input string.

    Returns:
        A dictionary mapping each character to its count.
    """
    lowertext = text.lower()
    char_count = {}
    for character in lowertext:
        if character in char_count:
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1
    return char_count

def average_word_length(text: str) -> float:
    """Calculates the average word length in the text.

    Punctuation is removed before calculation.

    Args:
        text: The input string.

    Returns:
        The average word length as a float. Returns 0 for empty text.
    """
    text = clear_punctuation(text)
    words = text.lower().split()
    if not words:
        return 0.0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def get_most_frequent_words(text: str, stop_words: Optional[List[str]] = None) -> Counter:
    """Finds the most frequent words in the text, excluding stop words.

    Args:
        text: The input string.
        stop_words: An optional list of words to exclude from the count.

    Returns:
        A Counter object with words and their frequencies.
    """
    if stop_words is None:
        stop_words = []
    
    text = clear_punctuation(text).lower()
    words = text.split()
    
    filtered_words = [word for word in words if word and word not in stop_words]
    return Counter(filtered_words)

def get_num_unique_words(text: str) -> int:
    """Counts the number of unique words in the text.

    Args:
        text: The input string.

    Returns:
        The total count of unique words.
    """
    text = clear_punctuation(text).lower()
    words = text.split()
    return len(set(word for word in words if word))

def get_longest_shortest_words(text: str) -> Tuple[str, str]:
    """Finds the longest and shortest words in the text.

    Args:
        text: The input string.

    Returns:
        A tuple containing the longest word and the shortest word.
        Returns ('', '') if the text is empty.
    """
    words = [word for word in clear_punctuation(text).lower().split() if word]
    if not words:
        return "", ""
    
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    return longest_word, shortest_word

def get_average_sentence_length(text: str) -> float:
    """Calculates the average sentence length in words.

    Sentences are assumed to be delimited by '.', '!', or '?'.

    Args:
        text: The input string.

    Returns:
        The average sentence length. Returns 0 for empty text.
    """
    processed_text = text.replace('!', '.').replace('?', '.')
    potential_sentences = processed_text.split('.')
    sentences = [s.strip() for s in potential_sentences if s.strip()]

    if not sentences:
        return 0.0
    
    total_words_in_sentences = sum(len(clear_punctuation(s).split()) for s in sentences)
    return total_words_in_sentences / len(sentences)

def display_stats(
    num_words: int, 
    char_count: Dict[str, int], 
    average_length: float, 
    frequent_words: Counter, 
    num_unique_words: int, 
    longest_word: str, 
    shortest_word: str, 
    avg_sentence_len: float
) -> None:
    """Prints a formatted report of all text statistics.

    Args:
        num_words: Total number of words.
        char_count: Dictionary of character counts.
        average_length: Average word length.
        frequent_words: Counter object of frequent words.
        num_unique_words: Total number of unique words.
        longest_word: The longest word found.
        shortest_word: The shortest word found.
        avg_sentence_len: Average sentence length.
    """
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
        if char.isalpha():
            print(f"{char}: {count}")
    print("-------- Most Frequent Words --------")
    # Display top 10 most frequent words
    for word, count in frequent_words.most_common(10):
        print(f"{word}: {count}")