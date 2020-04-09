"""Load a text file as a list.

Arguments:
­text file name (and directory path, if needed)

Exceptions:
­IOError if filename not found.

Returns:
­A list of all words in a text file in lower case.

Requires­:
import sys
"""

import sys

def load(file):
    """Open a file and return a list of lowercased words."""
    try:
        with open(file, 'r') as words_list:
            loaded_txt = words_list.read().strip().split("\n")
            loaded_txt = [word.lower() for word in loaded_txt]
            return loaded_txt
    except IOError as error_message:
        print("{}\nError loading {}. Terminating program.".format(
            error_message, file), 
              file=sys.stderr)
        sys.exit(1)
        