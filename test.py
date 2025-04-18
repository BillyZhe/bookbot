def get_letter_count(book):
    count_dict = {}
    for char in book:
        low = char.lower()
        count_dict[low] = count_dict.get(low,0) + 1
    return count_dict 
def get_order(dic):
    order_dic = {}
    order_dic = get_letter_count(reverse = True, key = get_order)
    return order_dic
def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        get_letter = get_letter_count(file_contents)
        for_order = get_order(get_letter_count)
    print(for_order)
main()

