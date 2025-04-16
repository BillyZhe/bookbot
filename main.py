from stats import get_word_count
from stats import get_letter_count
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        word_count = get_word_count(file_contents)
        letter_count = get_letter_count(file_contents)
        print(f"{word_count} words found in the document")
        print(letter_count)
main()
        