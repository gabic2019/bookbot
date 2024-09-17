def main():
    
    letters= dict()
    file = "books/frankenstein.txt"

    with open(file) as f:
        file_contents = f.read()

    book_length = len(file_contents.split())
    lower_file_contents = file_contents.lower()

    current_letter = "a"
    while ord(current_letter) <= ord("z"):
        #print(current_letter)
        letters[current_letter] = count(lower_file_contents, current_letter)
        current_letter = chr(ord(current_letter)+1)
    
    #print(letters)
    print(f"--- Begin report of {file} ---")
    print(f"{book_length} words found in the document")
    print()

    letters_list = [{"letter":k,"count":v} for k,v in letters.items()]
    #print(type(letters_list[0]))
    letters_list.sort(reverse=True, key=sort_on)

    for most_used_letter in letters_list:
        print(f"The '{most_used_letter['letter']}' character was found {most_used_letter['count']} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def count(file, letter):
    return len(file.split(letter))-1


main()


