def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_report = get_chars_dict_list(chars_dict)
    chars_report.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for char in chars_report:
        if char["char"].isalpha() == True:
            print(f"The {char["char"]} character was found {char["num"]} times")
    print("--- End report ---")
    
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()    


def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_chars_dict_list(chars_dict):
    chars_dict_list = []
    for key, value in chars_dict.items():
        chars_dict_list.append({"char" : key, "num" :value})
    return(chars_dict_list)
    
def sort_on(dict):
    return dict["num"]


main()