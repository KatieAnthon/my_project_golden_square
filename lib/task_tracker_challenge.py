""" user needs to keey track of tasks
chekc if text includes the string #TODO in given argument"""

""" 1 string paramater"""

""" use class structure to enable adding, removing and tracking"""
class Task_tracker():
    """ use init function"""
    def __init__(self):
        self.list_of_strings = []

        
        """ function to check for specific string"""
        """ returns True/ False for TODO string"""
        """ use 1 section to add tasks"""
    def add(self, string):
        if not string:
            raise Exception("can't add an empty string")
    
        if string not in self.list_of_strings and string == "#TODO":
            self.list_of_strings.append(string)
            self.result_string = ", ".join(self.list_of_strings)
            return "#TODO has been added"
        elif string.lower() not in self.list_of_strings:
            self.list_of_strings.append(string.lower())
            self.result_string = ", ".join(self.list_of_strings)
        else:
            pass

    def read(self):
        return self.result_string
        

    """ returns  task list when requested"""

    """ throws error if string entered is empty"""

    