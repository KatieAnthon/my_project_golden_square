""" a user wants to improve grammar
verify text starts with a capital letter
verify text starts with sentence ending puntuation mark"""


""" takes one argument as a string"""


def grammar_checker(string):
   # capital_letter = True
    #Ending_punctuation = True
    if not string:
          raise Exception("Can't check an empty string")

    
    """ function checks first letter is a capital"""
   
    """ function checks last letter is one of '.?!'"""
    """ returns True or False if the above conditions are met"""

    if string[0].isupper() and string[-1] in '.?!':
          return True
    elif string[0].isupper() and not string[-1] in '.?!':
          return f"Check the ending punctuation."
    elif string[-1] in '.?!' and not string[0].isupper():
          return f"Your starting capital letter is missing."
    else:
          return False

    """throws an error if there is an empty input for a string"""

    """ throws an error if a sentence starts with '.?!'"""