# Import the Counter class from the collections module
from collections import Counter

def main():
    """
    Main function that generates a report on the frequency of characters in a book.

    :return: None
    """
    # Specify the path to the book file
    book_path = "books/frankenstein.txt"
    # Get the text of the book
    text = get_book_text(book_path)
    # Get the number of words in the book
    num_words = get_num_words(text)
    # Get a dictionary of character frequencies
    chars_dict = get_chars_dict(text)
    # Sort the dictionary by value (frequency) in descending order
    chars_dict_sorted = chars_dict_to_sorted_list(chars_dict)

    # Generate a report on the character frequencies
    print(f"--- Begin report of {book_path} ---")

    print(f"\n{num_words} words found in the document\n")

    # Iterate over the sorted list and print each character and its frequency
    for char, count in chars_dict_sorted:
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report ---")


def get_num_words(text: str) -> int:
    """
    Returns the number of words in the given text.

    :param text: The text to count words in
    :return: The number of words in the text
    """
    # Split the text into words and return the length of the resulting list
    words = text.split()
    return len(words)


def get_book_text(path: str) -> str:
    """
    Returns the text of the book at the given path.

    :param path: The path to the book file
    :return: The text of the book
    """
    # Open the file and read its contents
    with open(path) as f:
        return f.read()


def get_chars_dict(text: str) -> dict:
    """
    Returns a dictionary of character frequencies in the given text.

    :param text: The text to count character frequencies in
    :return: A dictionary of character frequencies
    """
    # Remove non-alpha characters and convert to lowercase
    characters = ''.join(c for c in text if c.isalpha())
    # Use Counter to count the frequency of each character
    char_dict = Counter(characters.lower())
    return char_dict


def chars_dict_to_sorted_list(chars_dict: dict) -> list:
    """
    Returns a sorted list of tuples containing the character frequencies.

    :param chars_dict: A dictionary of character frequencies
    :return: A sorted list of tuples containing character frequencies
    """
    # Sort the dictionary by value (frequency) in descending order
    return sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    main()
