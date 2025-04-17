def get_word_count(book):
    words = book.split()
    return len(words)

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

