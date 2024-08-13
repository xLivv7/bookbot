def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(text)
    print("\n-------------------raport-------------------")
    print(f"\nwords: {num_words}\n")
    characters_with_counter = alph_for_raport(chars_dict)


def alph_for_raport(chars_dict):
    alphabet = []
    for key,value in chars_dict.items():
        if key.isalpha()==True:
            alphabet.append({"letter": key, "count": value})
    for dict in alphabet:
        print(f"letter '{dict['letter']}' was found {dict['count']} times in text")
    return alphabet
    

        
def sort_on(dict):
    return dict["num"]


    
def get_num_words(text):   
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered]+=1
        else:
            chars[lowered]=1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
