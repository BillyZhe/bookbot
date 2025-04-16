def get_letter_count(book):
    count_dict = []
    words = list(book)
    for char in words:
        low = char.lower()
        is_there = low in count_dict
        if is_there:
            count_dict[low] += 1            
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        get_letter = get_letter_count(file_contents)
    print(get_letter)
main()

