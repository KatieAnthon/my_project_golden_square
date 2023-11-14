#takes one argument
# returns first 5 words and appends "..."


def make_snippet(string):
    string_to_append = ""
    words = string.split(" ")
    if len(words) > 5:
        first_5_words = words[:5]
        for word in first_5_words:
            if word != first_5_words[-1]:
                string_to_append += (word + " ")
            else:
                string_to_append += word
        return string_to_append + "..."
    else:
        return string
