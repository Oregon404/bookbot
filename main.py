def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = (txt_words(text))
    word_count = get_word_count(words)
    chars = get_chars(words)
    unique_chars = set(chars)
    chars_count = get_char_count(chars, unique_chars)
    list = []
    for i in chars_count:
        list.append({"char" : i, "num" : chars_count[i]})
    list.sort(reverse=True, key=sort_on)
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document')
    print_chars(list)
    print("--- End report ---")
    #print(f'chars = {chars_count}')


def get_book_text(path):
    with open(path) as txt:
        return txt.read()

def txt_words(txt):
    return(txt.split())

def get_word_count(words):
    return(len(words))

def get_chars(txt):
    chars=[]
    txt = (''.join(char for char in txt if char.isalpha())).split()
    for i in range(0,len(txt)):
        chars.append((txt[i]).lower())
    return ''.join(chars)

def get_char_count(chars, uniq_chars):
    chars_count = {}
    for char in uniq_chars:
        char_count = chars.count(char)
        chars_count[char] = char_count
    return chars_count

def sort_on(dict):
    return dict["num"]

def print_chars(list):
    for i in list:
        print(f'The \'{i["char"]}\' character was found {i["num"]} times')  
main()