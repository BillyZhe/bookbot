def get_word_count(book):
    words = book.split()
    return len(words)

def get_letter_count(book):
    count_dict = {}
    for char in book:
        low = char.lower()
        count_dict[low] = count_dict.get(low,0) + 1
    return count_dict 

def get_order(diction):
    alpha = {}
    for key, value in diction.items():
        if str(key).isalpha():
            alpha[key] = value
    order = dict(sorted(alpha.items(), key = lambda x: x[1], reverse=True))
    return order  

