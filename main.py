from stats import get_num_words
from stats import get_num_letters

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(get_num_words(book_text, "me"))

    char_counts = get_num_letters(book_text)
    print(char_counts) 

if __name__ == "__main__":
    main()