
def get_num_words(book_text,word_to_count):
    words = book_text.split()
    total_words = len(words)
    occurrences = words.count(word_to_count)
    return f"Found {total_words} total words, and '{word_to_count}' occurs {occurrences} times."

def get_num_letters(book_text):
    text = book_text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count