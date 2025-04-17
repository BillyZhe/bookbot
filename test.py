def get_letter_count(book):
    count_dict = {}
    words = list(book)
    for char in words:
        low = char.lower()
        if count_dict.get(low) == None:
            count_dict.update({low: 1})
        else:
            count_dict[low] += 1
    return count_dict           
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        get_letter = get_letter_count(file_contents)
    print(get_letter)
main()

