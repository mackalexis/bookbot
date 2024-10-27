def main():
    path = 'books/frankenstein.txt'
    book_text = get_file_contents(path)
    num_words = get_word_count(book_text)
    char_count = count_chars(book_text)
    sorted_dict = sort_char_dict(char_count)
    print_report(num_words, sorted_dict)

def print_report(word_count, char_count_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char in char_count_list:
        print(f"The character {char['char']} appears {char['count']} times") 

    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def sort_char_dict(char_dict):
    sorted_dict = []
    for char in char_dict:
        sorted_dict.append({"char": char, "count": char_dict[char]})
        sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowered_text = text.lower()
    letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
    "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
    "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
    "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
    "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,
    " ": 0, "'": 0, ",": 0, ".": 0, "(": 0, ")": 0,
    "\n": 0, "\t": 0, "-": 0, ":": 0, ";": 0,
    "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
    "6": 0, "7": 0, "8": 0, "9": 0, "0": 0,
    "[": 0, "]": 0, "#": 0, "!": 0, "@": 0, "$": 0,
    "%": 0, "^": 0, "&": 0, "*": 0, "+": 0,
    "?": 0, "<": 0, ">": 0, '"': 0, "_": 0, "/": 0, "\\": 0}

    for char in lowered_text:
        #letters[char] += 1
        letters[char] = letters[char] + 1
    return letters

main()