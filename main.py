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
