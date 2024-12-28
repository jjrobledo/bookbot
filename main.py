def main():
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    num_words = count_words(text)
    char_list = convert_dict_to_list(count_characters(text))
    char_list.sort(reverse=True, key=sort_on)
    print_formatter(book_path, num_words, char_list)

def open_file(path):
    with open(path) as f:
        text = f.read()
        return text


def print_formatter(book_path, wordcount, chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount} words in the document")

    for char in chars:
        print(f"The {char['char']} character was found {char['count']} times")


def sort_on(dict):
    return dict["count"]


def count_words(text):
    word_count = len(text.split())
    return word_count


def convert_dict_to_list(dict):
    new_list = []
    for item in dict:
        if item.isalpha():
            new_dict = {}
            new_dict["char"] = item
            new_dict["count"] = dict[item]
            new_list.append(new_dict)

    return new_list


def count_characters(text):
    text = text.lower()
    character_counts = {}

    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts


main()
