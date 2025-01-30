def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(" ")
    print(f"{number_of_words} words found in the document")
    list_of_char = dict_to_list(chars_dict)
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    list_of_charaters = []

    for key in dict:
        num = dict[key]
        temp_dict = {"character": key, "num": num}
        list_of_charaters.append(temp_dict)
    list_of_charaters.sort(reverse=True, key=sort_on)
    for char in list_of_charaters:
        print(f"The '{char["character"]}' character was found {char["num"]} times")
        

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
    