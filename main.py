import sys
from stats import count_words
from stats import count_characters
from stats import sorted_dict

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()    
    except FileNotFoundError:
        return f"Error: file not found."
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    number_of_words = count_words(text)
    number_of_characters = count_characters(text.lower())
    sorted_characters = sorted_dict(number_of_characters)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
    return (
        f"----------- Word Count ----------\n"
        f"Found {number_of_words} total words\n"
        f"--------- Character Count -------\n"
        f"{sorted_characters}\n"
        f"============= END ==============="
    )
    
if __name__ == "__main__":
    print(main())