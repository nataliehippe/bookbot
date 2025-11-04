import sys
from stats import(
    sort_characters,
    get_num_letters,
    get_num_words
)

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Error: expected stdout to contain Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    print(get_num_words(book_text, "me"))

    char_counts = get_num_letters(book_text)
    sorted_charts = sort_characters(char_counts)
    for char,count in sorted_charts:
        if char.isalpha():
            print(f"{char}: {count}")

if __name__ == "__main__":
    main()