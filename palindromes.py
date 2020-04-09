"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dict

def main():
    word_list = load_dict.load('2of4brif.txt')
    palindrome_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)
    
    print("\nNumber of palindromes found: {}".format(len(palindrome_list)))
    print(*palindrome_list, sep='\n')


if __name__ == "__main__":
    main()
