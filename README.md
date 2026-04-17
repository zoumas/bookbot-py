# BookBot

BookBot is a CLI program that reads a book (plain text file) and prints a statistical report of word and character usage.

This is a guided project from [Boot.dev](https://www.boot.dev).

## Usage

```sh
python3 main.py <path_to_book>
```

### Example

```sh
python3 main.py books/frankenstein.txt
```

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
...
============= END ===============
```

Books are stored as `.txt` files in the `books/` directory (git-ignored).

## Project Structure

```
├── main.py    # Entry point — reads the book, runs analysis, prints report
├── stats.py   # Pure functions for word and character counting
└── books/     # Plain text book files (not committed)
```

## What I Learned

- **Reading files** — Opening and reading text files with Python's built-in `open()`.
- **String manipulation** — Splitting text into words, lowercasing, and iterating over characters.
- **Dictionaries** — Building frequency maps with `dict.get()` for default values.
- **Sorting** — Sorting dictionary items by value using `sorted()` with a `key` lambda.
- **Functions** — Breaking logic into small, reusable, well-typed functions across modules.
- **CLI arguments** — Using `sys.argv` to accept file paths from the command line.
- **Project structure** — Separating concerns across files and using `.gitignore` to keep data out of version control.
