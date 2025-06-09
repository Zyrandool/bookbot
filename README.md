# BookBot

BookBot is a simple command-line tool written in Python that analyzes the text of a book from a `.txt` file and generates a report with various statistics.

## About The Project

This project was built as part of the [Boot.dev](https://www.boot.dev) curriculum. The primary goal is to practice fundamental Python skills, including file I/O, string manipulation, and data structures, by creating a useful text analysis tool. It serves as a great introduction to building console-based applications in Python.

## Features

BookBot provides the following text statistics:

* Total word count
* Number of unique words
* Character frequency count (for alphabetic characters)
* Top 10 most frequent words (excluding common stop words)
* Average word length
* Average sentence length
* The longest and shortest words in the text

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3 installed on your system. You can check this by running:
```sh
python --version
```

### Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/zyrandool/bookbot.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd bookbot
    ```

3.  **Run the script:**
    Execute the `main.py` script from your terminal, providing the path to a book in `.txt` format as an argument. A sample book (`frankenstein.txt`) is included in the `books/` directory for testing.

    ```sh
    python3 main.py books/frankenstein.txt
    ```

## Sample Output

Running the script on a text file will produce a report similar to this:

```
============ BOOKBOT ============
Reading book from books/frankenstein.txt
=================================
----------- Stats ----------
Found 77986 total words
Found 6393 unique words
----------------------------
Average word length: 4.39 characters
Average sentence length: 22.18 words
Longest word: 'uninterruptedly' (15 chars)
Shortest word: 'a' (1 chars)
-------- Character Count --------
e: 45930
t: 30452
a: 27892
o: 26038
... (output truncated for brevity)
-------- Most Frequent Words --------
i: 3881
my: 1533
he: 1266
you: 1179
me: 938
his: 919
had: 887
have: 768
which: 746
him: 724
```

## Acknowledgements

* This project is based on the "BookBot" project from the [Boot.dev](https://www.boot.dev) backend developer career path.

