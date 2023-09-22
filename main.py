def main():
    book = "frankenstein"
    book_path = (f"books/{book}.txt")
    text = get_book_text(book_path)
    letters = letter_count(text)
    sorted_list = sort_letters(letters)
    print(f"---Begin report for the book {book}---")
    print(f"{count_words(text)} words were found in {book}")
    for item in sorted_list:
         print(f"The '{item['char']}' character was found {item['num']}")
    print ("-----END OF REPORT-----")

def get_book_text(book_path):
        with open(book_path) as f:
            return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)
         
def letter_count(text):
     text_lower = text.lower()
     word_list = text_lower.split()
     letter_dic = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0,
                   'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0,
                   's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
     for word in word_list:
          for letter in word:
               if letter in letter_dic:
                    letter_dic[letter] += 1 
     return letter_dic

def sort_on(d):
    return d["num"]

def sort_letters(letter_dic):
     letter_list = []
     for letter in letter_dic:
          letter_list.append({"char" : letter, "num" : letter_dic[letter]})
     letter_list.sort(reverse=True, key=sort_on)
     return letter_list
     

main()