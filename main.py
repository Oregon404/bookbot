def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(text)
    print(f'The word count is {word_count} words')


def get_book_text(path):
    with open(path) as txt:
        return txt.read()

def txt_words(txt):
    return(txt.split())

def get_word_count(txt):
    return(len(txt_words(txt)))

main()