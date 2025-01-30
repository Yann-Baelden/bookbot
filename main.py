def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_char = get_num_characters(text)
    print(num_char)

def get_num_characters(text):
    lower_text = text.lower()
    characters = []
    num_characters = {}
    for character in lower_text:
        if character in characters:
            num_characters[character] +=1
        else:
            characters.append(character)
            num_characters[character] = 1
    return num_characters

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
    