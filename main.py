import sys
from stats import get_sorted_character_counts

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def count_words(text):
    return len(text.split())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)

    num_words = count_words(book_text)

    sorted_char_counts = get_sorted_character_counts(book_text)

    print("=" * 30 + " BOOKBOT " + "=" * 30)
    print(f"Analyzing book found at {filepath}...")
    print("-" * 30 + " Word Count " + "-" * 30)
    print(f"Found {num_words} total words")
    print("-" * 29 + " Character Count " + "-" * 29)

    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['count']}")

    print("=" * 32 + " END " + "=" * 32)

if __name__ == "__main__":
    main()
