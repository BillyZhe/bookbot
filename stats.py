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
    final = []
    for key, value in diction.items():
        if str(key).isalpha():
            char_dict = {"character": key, "count": value}
            final.append(char_dict)
        
        final.sort(key = lambda item: item["count"], reverse=True)
    return final

