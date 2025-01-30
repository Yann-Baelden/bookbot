def main():
    count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        count += 1
    print(count)

main()
    