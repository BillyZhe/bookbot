def get_word_count(book):
    words = book.split()
    return len(words)
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        word_count = get_word_count(file_contents)
        print(f"{word_count} words found in the document")
main()
        