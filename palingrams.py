"""Find all word­pair palingrams in a dictionary file."""

import load_dict

def main():
    word_list = load_dict.load('2of4brif.txt')
    palingrams = find_palingrams(word_list)
    palingrams_sorted = sorted(palingrams)
    print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
    for first, second in palingrams_sorted:
        print("{} {}".format(first, second))


def find_palingrams(word_list):
    palingram_list = []
    words = set(word_list)
    for word in words:
        last_letter_index = len(word)
        reversed_word = word[::-1]
        if last_letter_index > 1:
            for i in range(last_letter_index):
                if word[i:] == reversed_word[:last_letter_index-i] and \
                  reversed_word[last_letter_index-i:] in words:
                    palingram_list.append((word,reversed_word[last_letter_index-i:]))
                if word[:i] == reversed_word[last_letter_index-i:] and \
                  reversed_word[:last_letter_index-i] in words:
                    palingram_list.append((reversed_word[:last_letter_index-i],word))

    return palingram_list


if __name__ == "__main__":
    main()
