def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    alphachar_dict = clean_alpha(chars_dict)
    report(book_path, num_words, alphachar_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def clean_alpha(text):
    keys_to_remove = [key for key in text.keys() if not key.isalpha()]
    for key in keys_to_remove:
        del text[key]
    return text


def report(bookpath, num_words, text):
    print(f"--- Begin report of {bookpath} ---")
    print(f"{num_words} words found in the document")
    sorted_dict = sorted(text.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_dict:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
