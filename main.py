from stats import count_words, count_characters


def main():
    contents = get_book_text("books/frankenstein.txt")

    num_words = count_words(contents)
    print(f"Found {num_words} total words")

    print(count_characters(contents))


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


main()
