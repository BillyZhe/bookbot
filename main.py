import sys
from stats import get_word_count
from stats import get_letter_count
from stats import get_order
def main():
        if len(sys.argv) > 1:
            file_contents = sys.argv[1]
            with open(file_contents, "r") as file:
                book = file.read()
            word_count = get_word_count(book)
            letter_count = get_letter_count(book)
            ordered = get_order(letter_count) 
            print(f"============ BOOKBOT ============")
            print(f"Analyzing book found at {sys.argv[1]}")
            print(f"----------- Word Count ----------")
            print(f"Found {word_count} total words")
            print(f"--------- Character Count -------")
            for letter_count in ordered:
                character = letter_count["character"]
                count = letter_count["count"]
                print(f"{character}: {count}")
            print(f"============= END ===============")
        else:
            print(f"Usage: python3 main.py <path_to_book>")
            return sys.exit(1)
main()
        