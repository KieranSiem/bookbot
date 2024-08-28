def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    list_of_char_counts = convert_dict_of_chars_to_list(char_count)
    generate_report(book_path, num_words, list_of_char_counts)

def sort_on(dict):
    return dict['char_count']

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    lower_case_text = text.lower()
    list_of_lower_case = lower_case_text.split()
    
    dict_of_char_counts = {}

    for word in list_of_lower_case:
        for char in word:
            if dict_of_char_counts.get(char) is None:
                dict_of_char_counts[char] = 1
            else:
                dict_of_char_counts[char] += 1
    
    return dict_of_char_counts

def convert_dict_of_chars_to_list(char_count):
    list_of_counts = [] 
    for char in char_count:
        new_dict = {}
        if char.isalpha():
            new_dict['character'] = char
            new_dict['char_count'] = char_count[char]
            list_of_counts.append(new_dict)
        else:
            continue

    list_of_counts.sort(reverse=True, key=sort_on)

    return list_of_counts

def generate_report(book_path, num_words, list_of_char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in list_of_char_counts:
        print(f"The {char['character']} character was found {char['char_count']} times")


main()
