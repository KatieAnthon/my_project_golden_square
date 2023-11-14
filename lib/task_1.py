''' the problem:
user needs to manage time 
provide an estmate of reading time for a text
can read 200 words per minute'''

# 1 paramater needed 
# return hours required to read
import math

def reading_time(string):
    if not string:
        raise Exception("Can't estimate time for empty text!")
    '''removes delimeters from string and separates each word into a list'''
    clean_string = string.replace(',', ' ')
    cleaner_string = clean_string.replace('-', ' ')
    final_words = cleaner_string.split(' ')
    ''' counts number of words'''
    number_of_words= len(final_words)
    '''calculates time based off of words'''
    if number_of_words != 0:
        minutes_spent_reading = math.floor(number_of_words/200)
        '''converts min to hours if it meets the threshold'''
        if minutes_spent_reading >= 60:
            hours_spend_reading = math.floor(minutes_spent_reading/60)
            return f"Reading time = {hours_spend_reading} Hours"
        else:
            return f"Reading time = {minutes_spent_reading} Minutes"
    else:
        raise Exception("Can't estimate time for empty text!")
    
    ''' a string with time'''


    '''there shouldnt be any side effects'''