# function to count words in a string
import re
def count_words(string):
    clean_string = string.replace(',', " ")
    clean_string2 = clean_string.replace("-", " ")
    list_by_spaces = clean_string2.split(" ")
    return len(list_by_spaces)