def main():
    book = "frankenstein"
    book_path = (f"books/{book}.txt")
    text = get_book_text(book_path)
    print(f"{count_words(text)} words were found in the document {book}")

def get_book_text(book_path):
        with open(book_path) as f:
            return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)
         

main()