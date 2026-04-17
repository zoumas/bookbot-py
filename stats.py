def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    d = {}
    for char in text.lower():
        d[char] = d.get(char, 0) + 1
    return d


def sorted_characters(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
