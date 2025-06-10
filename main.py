from stats import get_book_text
from stats import count_characters
from stats import sort_it
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    
    returned_values = get_book_text(path)
    ##print(returned_values)
    words = returned_values.split()
    count_words = 0

    for i in words:
        count_words += 1

    ##print(f"{count_words} words found in the document")

    check = count_characters(path)
    ##print(check)
    sorting = sort_it(check)
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for i in sorting:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
        

main()