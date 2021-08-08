"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate the required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""



from collections import Counter, OrderedDict
import itertools

"""
Counter: creates a dictionary of characters from the strings as keys and
the number of each particular character as values.

Sorted: sorts the dictionary keys alphabetically.
    
OrderedDict: preserves the order in which the keys are inserted.

Itertools Dropwhile: function returns an iterator only after the function
in the argument returns false for the first time.

# If each value in the ordered_characters dict is greater than or equal to
each value in the ordered_phrase dict, the result is an empty list and
True is returned.
# Otherwise, result stores the character(s) from the
ordered_phrase dict where the values do not match the ordered_characters
dict and False is returned.
    
"""

characters = "cbacba"
phrase = "aabbccc"

def generate_phrase2(characters, phrase):

    ordered_characters = OrderedDict(sorted(Counter(characters).items(), key=lambda c: c[0]))
    ordered_phrase = OrderedDict(sorted(Counter(phrase).items(), key=lambda p: p[0]))

    try:
        result = list(itertools.dropwhile(lambda k: ordered_characters[k] >= ordered_phrase[k], ordered_phrase))
        print(result)
        return False if result != [] else True
        
    except KeyError:
        return False
    
print(generate_phrase2(characters, phrase))
