import sys
from stats import count_words, count_characters, sorted_characters


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {filepath}...")
    contents = get_book_text(filepath)

    num_words = count_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count = sorted_characters(count_characters(contents))
    for item in char_count:
        char = item[0]
        if not char.isalpha():
            continue
        num = item[1]
        print(f"{char}: {num}")

    print("============= END ===============")


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


main()
