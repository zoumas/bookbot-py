# Copilot Instructions

## Project Overview

Bookbot is a Python CLI program that reads a book (plain text file) and prints a statistical report of word and character usage.

## Running

```sh
python3 main.py
```

## Architecture

- `main.py` — Entry point. Reads the book file, runs analysis, and prints the report.
- Books are stored as `.txt` files (e.g., `books/frankenstein.txt`). These are not committed to the repo.

## Conventions

- Pure Python with no external dependencies — use only the standard library.
- This is a Boot.dev guided project. Tests are run externally via the `bootdev` CLI, not within the repo.
