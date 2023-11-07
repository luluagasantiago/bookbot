
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letters = count_letters(text)
    print(print_report_book(letter_count=letters, word_count=num_words,book_name=book_path))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text:str):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha(): 
           if letter in letters:
               letters[letter] += 1
           else:
               letters[letter] = 1
    return letters

def print_report_book(letter_count: dict, word_count: int, book_name: str):
    print(f"Analyzing the book: {book_name}. . .")
    print(f"{word_count} words found in the document!")
    ordered_letters = sorted(list(letter_count.keys()))
    for l in ordered_letters:
        print(f"The letter {l} was found {letter_count[l]} times!")
            
main()
