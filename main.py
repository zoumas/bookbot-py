def main():
    contents = get_book_text("books/frankenstein.txt")

    print(contents)


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


main()
