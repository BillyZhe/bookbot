from stats import get_word_count
from stats import get_letter_count
from stats import get_order
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        word_count = get_word_count(file_contents)
        letter_count = get_letter_count(file_contents)
        ordered = get_order(letter_count) 
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        print(f"----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print(f"--------- Character Count -------")
        for letter_count in ordered:
            character = letter_count["character"]
            count = letter_count["count"]
            print(f"{character}: {count}")
        print(f"============= END ===============")
main()
        