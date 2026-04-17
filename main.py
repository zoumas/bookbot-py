def main():
    contents = get_book_text("books/frankenstein.txt")

    num_words = count_words(contents)
    print(f"Found {num_words} total words")


def count_words(text: str) -> int:
    return len(text.split())


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


main()
