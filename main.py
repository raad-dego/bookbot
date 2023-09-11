def count_words(text):
    return len(file_content.split())


def count_characters(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    char_count = {}
    for char in text:
        # Adding key value pairs to the dict and
        # assigning 1 if not in dict
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{count_words(text)} words found in the document')
    dict_char = count_characters(text)
    for char, times in sorted(dict_char.items(), key=lambda dict_char: dict_char[0]):
        print(f"The {char} character was found {times} times")
    print("--- End report ---")


with open("books/frankenstein.txt") as f:
    file_content = f.read()
    report(file_content)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()