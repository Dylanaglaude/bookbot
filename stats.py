def get_sorted_character_counts(text):
    char_counts = {}

    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1

    sorted_char_list = sorted(
        [{"char": char, "count": count} for char, count in char_counts.items()],
        key=lambda x: x["count"],
        reverse=True
    )

    return sorted_char_list

